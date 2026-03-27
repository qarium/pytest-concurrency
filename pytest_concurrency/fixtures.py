import threading
import typing as t

from _pytest import fixtures

# pylint: disable=invalid-name
# noqa: B009 — intentional defensive access to pytest internal class
FixtureDef: t.Any = getattr(fixtures, "FixtureDef")  # noqa: B009


@t.final
class ThreadLocalFixtureDef(threading.local, FixtureDef):
    pass


def patch_pytest_fixtures() -> None:
    fixtures.FixtureDef = ThreadLocalFixtureDef
