import threading
import typing as t

from _pytest import fixtures

# pylint: disable=invalid-name
FixtureDef: t.Any = getattr(fixtures, 'FixtureDef')


@t.final
class ThreadLocalFixtureDef(threading.local, FixtureDef):
    pass


def patch_pytest_fixtures() -> None:
    fixtures.FixtureDef = ThreadLocalFixtureDef
