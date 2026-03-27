# pytest-concurrency

A pytest plugin for parallel test execution with configurable concurrency.

## Installation

```bash
pip install pytest-concurrency
```

## Quick Start

```bash
# Run tests with 4 parallel workers
pytest --workers 4

# Auto-detect CPU cores
pytest --workers auto

# Via environment variable
PYTEST_CONCURRENCY_WORKERS=4 pytest
```

## Documentation

Full documentation is available at [https://qarium.github.io/pytest-concurrency/](https://qarium.github.io/pytest-concurrency/)