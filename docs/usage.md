# Usage Guide

This guide covers how to use pytest-concurrency in your test suite.

## Basic Usage

### Command Line

Enable parallel execution by passing the `--workers` option to pytest

```bash
pytest --workers 4
```

### Environment Variable

Alternatively, set the number of workers via environment variable

```bash
export PYTEST_CONCURRENCY_WORKERS=4
pytest
```

### Auto-Detection

Use `auto` to automatically detect and number of CPU cores

```bash
pytest --workers auto
```

## How It Works

When enabled, pytest-concurrency

1. **Patches pytest internals** — Makes `SetupState`, `FixtureDef`, and `os.environ` thread-local
2. **Distributes tests across workers** — Uses round-robin scheduling to balance load
3. **Executes tests in parallel** — Each worker runs its assigned tests in a separate thread
4. **Collects results** — Test results are aggregated and reported normally

## Test Distribution

Tests are sorted by their `nodeid` and distributed across workers using round-robin scheduling

### Parametrized Tests

Parametrized tests with the same base test function are grouped together and executed on the same worker
to ensure that fixture setup/teardown runs correctly for related test cases.

## Integration with Allure

pytest-concurrency automatically patches allure reporting to be thread-safe

```bash
pip install pytest-concurrency[allure]
```

When allure is installed, the plugin provides thread-safe versions of

- `AllureListener`
- `AllureReporter`
- `ThreadContextItems`

This ensures that allure reports from parallel tests don't interfere with each other.

## Best Practices

### Thread Safety

- Avoid shared mutable state in tests
- Use fixtures for test isolation
- Be cautious with global state modifications

### Performance

- Start with a worker count equal to your CPU cores
- Adjust based on test characteristics (I/O vs CPU-bound)
- Consider memory constraints when increasing worker count

### Debugging

- Use `--workers 1` to disable parallelization for debugging
- Check test isolation by running subsets independently