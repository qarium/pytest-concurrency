import os
import sys
import typing as t
from threading import Thread

import pytest
from _pytest.main import Session
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.terminal import TerminalReporter

from . import envvars
from .runner import (
    run_test_suite,
    create_test_suites,
    patch_pytest_runner,
)
from .system import patch_os
from .allure import patch_allure
from .tools import get_workers_count
from .fixtures import patch_pytest_fixtures

WORKERS_ARGUMENT: t.Final = '--workers'
PLUGIN_IS_ENABLED: t.Final = list(filter(lambda x: WORKERS_ARGUMENT in x, sys.argv)) or \
                             envvars.PYTEST_CONCURRENCY_WORKERS in os.environ


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup('pytest-concurrency')

    group.addoption(WORKERS_ARGUMENT,
                    type=int,
                    dest='workers',
                    help='Workers count',
                    default=os.getenv(envvars.PYTEST_CONCURRENCY_WORKERS))
    group.addoption('--worker-timeout',
                    type=int,
                    dest='worker_timeout',
                    help='Worker timeout',
                    default=os.getenv(envvars.PYTEST_CONCURRENCY_WORKER_TIMEOUT))


if PLUGIN_IS_ENABLED:
    patch_os()
    patch_pytest_runner()
    patch_pytest_fixtures()
    patch_allure()

    TerminalReporter.pytest_runtest_logstart = lambda *a, **k: None


    @pytest.mark.trylast
    def pytest_configure(config: Config) -> None:
        reporter = config.pluginmanager.getplugin('terminalreporter')

        for reporter_option in ('_showfspath', '_show_progress_info'):
            setattr(reporter, reporter_option, False)


    @pytest.hookimpl
    def pytest_runtestloop(session: Session) -> bool:
        continue_on_collection_errors = session.config.option.continue_on_collection_errors

        if session.testsfailed and not continue_on_collection_errors:
            error_suffix = 's' if session.testsfailed != 1 else ''
            raise session.Interrupted(f'{session.testsfailed} error{error_suffix} during collection')

        if session.config.option.collectonly:
            return True

        workers_count = get_workers_count(session.config,
                                          WORKERS_ARGUMENT)
        test_suites = create_test_suites(session, workers_count)

        workers = []

        for test_suite in test_suites:
            if not test_suite:
                continue

            worker = Thread(target=run_test_suite,
                            args=(session, test_suite))
            workers.append(worker)
            worker.start()
        for worker in workers:
            worker.join(timeout=session.config.option.worker_timeout)

        return True
