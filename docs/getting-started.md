# Getting Started

## Installation

```bash
pip install pytest-concurrency
```

## Basic Usage

### Enable Parallel Execution

```bash
# Run with 4 workers
pytest --workers 4

# Auto-detect CPU count
pytest --workers auto
```

### Environment Variables

You can also configure workers via environment variable:

```bash
PYTEST_CONCURRENCY_WORKERS=4 pytest
```

## How It Works

When `--workers` is provided or `PYTEST_CONCURRENCY_WORKERS` is set, the plugin:

1. **Patches pytest internals** — makes `SetupState`, `FixtureDef`, and `os.environ` thread-local
2. **Collects all tests** — standard pytest collection
3. **Groups parametrized tests** — keeps same test function with different params together
4. **Distributes across workers** — round-robin assignment for balanced load
5. **Runs in parallel threads** — each worker executes its test suite

## Compatibility

- Python 3.10+
- pytest 7.0+
- `gevent` and `pytest-gevent` (required, installed automatically with the plugin)
- Optional: `allure-pytest` for Allure integration

## Limitations

- Tests must be thread-safe (no shared mutable state)
- Fixtures should not rely on process-level state
- Some pytest plugins may be incompatible with threading