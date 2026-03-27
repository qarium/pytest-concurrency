import os
import threading
import typing as t

PYTEST_CURRENT_TEST_ENV: t.Final = "PYTEST_CURRENT_TEST"

# pylint: disable=invalid-name
Environ: t.Any = os._Environ


class ThreadLocalEnviron(Environ):
    def __init__(self, env: Environ):
        data = env._data

        super().__init__(data, env.encodekey, env.decodekey, env.encodevalue, env.decodevalue)

        self.putenv = os.putenv
        self.unsetenv = os.unsetenv

        self.thread_store = getattr(env, "thread_store", threading.local())

    def __getitem__(self, key: str) -> str:
        if key == PYTEST_CURRENT_TEST_ENV:
            if hasattr(self.thread_store, key):
                value = getattr(self.thread_store, key)

                return self.decodevalue(value)
            raise KeyError(key)
        return super().__getitem__(key)

    def __setitem__(self, key: str, value: str) -> None:
        if key == PYTEST_CURRENT_TEST_ENV:
            value = self.encodevalue(value)
            self.putenv(self.encodekey(key), value)

            return setattr(self.thread_store, key, value)
        return super().__setitem__(key, value)

    def __delitem__(self, key: str) -> None:
        if key == PYTEST_CURRENT_TEST_ENV:
            self.unsetenv(self.encodekey(key))

            if hasattr(self.thread_store, key):
                return delattr(self.thread_store, key)

            raise KeyError(key)
        return super().__delitem__(key)

    def __iter__(self) -> t.Generator[str, None, None]:
        if hasattr(self.thread_store, PYTEST_CURRENT_TEST_ENV):
            yield PYTEST_CURRENT_TEST_ENV

        keys = list(self._data)

        for key in keys:
            yield self.decodekey(key)

    def __len__(self) -> int:
        return len(self.thread_store.__dict__) + len(self._data)

    def copy(self) -> "Environ":
        return self.__class__(self)


def patch_os() -> None:
    os.environ = ThreadLocalEnviron(os.environ)  # noqa: B003
