# Configuration

## Command-Line Options

### `--workers`

Number of parallel workers for test execution.

```bash
pytest --workers 4
pytest --workers auto  # Uses CPU count
```

**Default:** Plugin disabled (sequential execution)

**Values:**

| Value | Description |
|-------|-------------|
| `N` (int) | Run with exactly N workers |
| `auto` | Auto-detect using `os.cpu_count()` |

### `--worker-timeout`

Timeout in seconds for worker thread completion.

```bash
pytest --workers 4 --worker-timeout 300
```

**Default:** `None` (no timeout)

## Environment Variables

### `PYTEST_CONCURRENCY_WORKERS`

Enable parallel execution and set worker count.

```bash
export PYTEST_CONCURRENCY_WORKERS=4
pytest  # Runs with 4 workers
```

**Values:** Same as `--workers` CLI option

### `PYTEST_CONCURRENCY_WORKER_TIMEOUT`

Set worker timeout via environment.

```bash
export PYTEST_CONCURRENCY_WORKER_TIMEOUT=300
pytest  # Workers timeout after 5 minutes
```

## Priority

CLI options take precedence over environment variables:

1. `--workers` CLI option
2. `PYTEST_CONCURRENCY_WORKERS` environment variable
3. Plugin disabled (sequential execution)

## Test Distribution

Tests are distributed using **round-robin** algorithm:

1. All tests are sorted by `nodeid`
2. Parametrized tests with the same `module.class.function` are grouped together
3. Groups are distributed across workers in round-robin fashion

This ensures:

- Balanced load across workers
- Setup/teardown consistency for parametrized tests
- Deterministic distribution (same tests always go to same worker)