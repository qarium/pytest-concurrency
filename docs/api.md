# API Reference

This document describes the public API of pytest-concurrency.

## Plugin Hooks

### pytest_addoption

Registers command line options for the plugin

```python
def pytest_addoption(parser: Parser) -> None
```

**Arguments:**
- `parser` — pytest's argument parser

**Options added:**
- `--workers` — Number of parallel workers (int or "auto")
- `--worker-timeout` — Timeout for worker threads in seconds (int)

### pytest_configure

Configures the plugin when enabled

```python
@pytest.mark.trylast
def pytest_configure(config: Config) -> None
```

**Behavior:**
- Disables verbose reporter options for cleaner output

### pytest_runtestloop

Replaces the default test loop with parallel execution

```python
@pytest.hookimpl(trylast=True)
def pytest_runtestloop(session: Session) -> bool:
```

**Arguments:**
- `session` — pytest session object

**Returns:** `True` (indicates the loop was handled)

**Behavior:**
- Checks for collection errors
- Handles collect-only mode
- Distributes tests across workers
- Executes tests in parallel
- Waits for all workers to complete

## Utility Functions

### get_workers_count

Determines the number of workers to use

```python
from pytest_concurrency.tools import get_workers_count

count = get_workers_count(config, "workers", default=1)
```

**Arguments:**
- `config` — pytest config object
- `arg_name` — Name of the config option
- `default` — Default value if not specified (default: 1)

**Returns:** `int` — Number of workers

**Special values:**
- `"auto"` — Returns the number of CPU cores
- `None` — Returns the default value

## Patch Functions

### patch_os

Makes `os.environ` thread-local

```python
from pytest_concurrency.system import patch_os

patch_os()
```

### patch_pytest_runner

Makes pytest's `SetupState` thread-local

```python
from pytest_concurrency.runner import patch_pytest_runner

patch_pytest_runner()
```

### patch_pytest_fixtures

Makes pytest's `FixtureDef` thread-local

```python
from pytest_concurrency.fixtures import patch_pytest_fixtures

patch_pytest_fixtures()
```

### patch_allure

Makes allure reporting thread-safe (only when allure is installed)

```python
from pytest_concurrency.allure import patch_allure

patch_allure()
```