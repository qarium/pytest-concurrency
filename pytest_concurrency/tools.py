import os
import typing as t

from _pytest.config import Config

DEFAULT_WORKERS_COUNT: t.Final = 1


def get_workers_count(config: Config,
                      arg_name: str,
                      default: int = DEFAULT_WORKERS_COUNT) -> int:
    count = config.getoption(arg_name)

    if count == 'auto':
        count = os.cpu_count() or default

    return int(count)
