# pytest-concurrency

A pytest plugin for parallel test execution with configurable concurrency.

## Overview

pytest-concurrency enables you to run your tests in parallel using multiple worker threads.
This can significantly reduce test execution time for test suites with many independent tests.

## Features

- **Parallel test execution** — Run tests concurrently using multiple worker threads
- **Configurable concurrency** — Control the number of parallel workers via CLI or environment variable
- **Automatic load balancing** — Tests are distributed across workers using round-robin scheduling
- **Allure integration** — Thread-safe reporting when using pytest-allure
- **Gevent support** — Compatible with gevent for async test scenarios

## Installation

```bash
pip install pytest-concurrency
```

## Quick Start

Enable parallel test execution by adding the `--workers` option:

```bash
pytest --workers 4
```

Or set the environment variable

```bash
export PYTEST_CONCURRENCY_WORKERS=4
pytest
```

## Documentation

- [Usage Guide](usage.md) — Detailed usage instructions and examples
- [API Reference](api.md) — Public API documentation
- [Configuration](configuration.md) — Configuration options and environment variables