# API Reference

## Public Functions

### `get_workers_count`

```python
def get_workers_count(
    config: Config,
    arg_name: str,
    default: int = DEFAULT_WORKERS_COUNT
) -> int
```

Determine the number of workers from pytest config.

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `config` | `Config` | pytest configuration object |
| `arg_name` | `str` | Argument name to query |
| `default` | `int` | Default count when auto-detection fails (default: 1) |

**Returns:** `int` — Number of workers

**Behavior:**

- If value is an integer — returns it directly
- If value is `"auto"` — returns `os.cpu_count()` or `default` if CPU count is unavailable

**Example:**

```python
from pytest_concurrency.tools import get_workers_count
from _pytest.config import Config

workers = get_workers_count(config, "workers", default=2)
```

## Plugin Hooks

### `pytest_addoption`

Registers the plugin's command-line options:

- `--workers` — Number of parallel workers (int or "auto")
- `--worker-timeout` — Timeout for worker threads (seconds)

### `pytest_runtestloop`

Custom test execution loop that:

1. Creates test suites for each worker
2. Spawns worker threads
3. Runs tests in parallel
4. Waits for completion with timeout

## Patching Functions

!!! warning "Internal"
    pytest-concurrency patches internal pytest classes at module level when the plugin is enabled. Do not call these directly.

| Function | Module | Purpose |
|----------|--------|---------|
| `patch_os` | `system.py` | Makes `os.environ` thread-local |
| `patch_pytest_runner` | `runner.py` | Makes `SetupState` thread-local |
| `patch_pytest_fixtures` | `fixtures.py` | Makes `FixtureDef` thread-local |
| `patch_allure` | `allure.py` | Makes Allure classes thread-local (optional) |