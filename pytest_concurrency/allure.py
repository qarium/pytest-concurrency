import sys
import threading
import typing as t

try:
    import allure_pytest.plugin
    import allure_commons.reporter

    from allure_pytest.listener import AllureListener
    from allure_commons.reporter import AllureReporter, ThreadContextItems


    class ThreadLocalAllureListener(threading.local, AllureListener):
        def __init__(self, *args: t.List[t.Any], **kwargs: t.Dict[t.Any, t.Any]) -> None:
            super().__init__(*args, **kwargs)


    class ThreadLocalAllureReporter(threading.local, AllureReporter):
        def __init__(self, *args: t.List[t.Any], **kwargs: t.Dict[t.Any, t.Any]) -> None:
            super().__init__(*args, **kwargs)


    class ThreadContextItemsWithGeventSupport(ThreadContextItems):
        if 'gevent' in sys.modules:
            def cleanup(self) -> None:
                pass


    def patch_allure() -> None:
        allure_pytest.plugin.AllureReporter = ThreadLocalAllureReporter
        allure_pytest.plugin.AllureListener = ThreadLocalAllureListener
        allure_commons.reporter.ThreadContextItems = ThreadContextItemsWithGeventSupport
except ImportError:
    def patch_allure() -> None:
        pass
