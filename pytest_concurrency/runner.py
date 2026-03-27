import threading
import typing as t

from _pytest import runner
from _pytest.main import Session
from _pytest.nodes import Item


@t.final
class ThreadLocalSetupState(threading.local, runner.SetupState):
    pass


def patch_pytest_runner() -> None:
    runner.SetupState = ThreadLocalSetupState


def _get_next_item(collection: list[t.Any], index: int) -> t.Optional[t.Any]:
    next_index = index + 1

    if len(collection) <= next_index:
        return None

    return collection[next_index]


def _create_test_cases(items: list[Item]) -> t.Generator[tuple[t.Any, ...], None, None]:
    test_cases: list[Item] = []

    def item_unique_key(item: Item) -> str:
        cls = item.cls
        module = item.module

        test_name = item.originalname
        cls_name = cls.__name__ if cls else "Function"

        return f"{module.__name__}.{cls_name}.{test_name}"

    def can_be_merged(item_one: Item, item_two: Item) -> bool:
        return item_unique_key(item_one) == item_unique_key(item_two)

    for index, current_item in enumerate(items):
        next_item = _get_next_item(items, index)

        if test_cases:
            last_item = test_cases[-1]

            if can_be_merged(last_item, current_item):
                test_cases.append(current_item)
                continue

            yield tuple(test_cases)

            test_cases = []

        if next_item and can_be_merged(current_item, next_item):
            test_cases.append(current_item)
            continue

        yield (current_item,)

    if test_cases:
        yield tuple(test_cases)


def create_test_suites(session: Session, workers_count: int) -> list[list[tuple[Item, ...]]]:
    # nodeid uniquely identifies a test as file::class::function[params]
    session.items.sort(key=lambda i: i.nodeid)
    test_suites: list[list] = [[] for _ in range(workers_count)]

    suite_index = 0

    for test_case in _create_test_cases(session.items):
        test_suites[suite_index].append(test_case)

        suite_index += 1

        if suite_index > len(test_suites) - 1:
            suite_index = 0

    return test_suites


def _run_item(session: Session, item: Item, next_item: t.Optional[Item]) -> None:
    item.ihook.pytest_runtest_protocol(item=item, nextitem=next_item)

    if session.shouldstop:
        raise session.Interrupted(session.shouldstop)

    if session.shouldfail:
        raise session.Failed(session.shouldfail)


def run_test_suite(session: Session, test_suite: list[tuple[Item, ...]]) -> None:
    for test_index, test_case in enumerate(test_suite):
        next_collection = test_suite[test_index + 1] if test_index + 1 < len(test_suite) else None

        for item_index, item in enumerate(test_case):
            if len(test_case) == 1:
                next_item = next(iter(next_collection)) if next_collection else None
                _run_item(session, item, next_item)
                continue

            next_item = (
                test_case[item_index + 1]
                if item_index + 1 < len(test_case)
                else next(iter(next_collection))
                if next_collection
                else None
            )
            _run_item(session, item, next_item)
