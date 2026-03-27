# Configuration

This document describes the configuration options for pytest-concurrency.

## Command Line Options

### --workers

Number of parallel worker threads

```bash
pytest --workers 4
```

**Values:**
- Integer (e.g., `4`) — Number of workers
- `"auto"` — Use number of CPU cores
- Not specified — Plugin disabled (sequential execution)

### --worker-timeout

Timeout in seconds for worker threads

```bash
pytest --worker-timeout 60
```

**Default:** None (workers run indefinitely)

## Environment Variables

### PYTEST_CONCURRENCY_WORKERS

Number of parallel workers

```bash
export PYTEST_CONCURRENCY_WORKERS=4
pytest
```

**Values:**
- Integer (e.g., `4`) — Number of workers
- `"auto"` — Use number of CPU cores
- `--worker-timeout` in CLI or `PYTEST_CONCURRENCY_WORKER_TIMEOUT` env var — timeout value

### PYTEST_CONCURRENCY_WORKER_TIMEOUT

Timeout in seconds for worker threads

```bash
export PYTEST_CONCURRENCY_WORKER_TIMEOUT=60
pytest
```

**Default:** None

## pyproject.toml

Add to your `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"
```

## Priority

Configuration priority (highest to lowest)

1. Command line options (`--workers`, `--worker-timeout`)
2. Environment variables (`PYTEST_CONCURRENCY_WORKERS`, `PYTEST_CONCURRENCY_WORKER_TIMEOUT`)
3. Default values