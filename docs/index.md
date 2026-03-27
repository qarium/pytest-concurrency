# pytest-concurrency

A pytest plugin for parallel test execution with configurable concurrency.

## Features

- **Parallel test execution** — run tests concurrently using multiple workers
- **Thread-safe pytest internals** — patches pytest's internal state for thread isolation
- **Optional Allure integration** — works with allure-pytest when installed
- **Auto-detection** — automatically use CPU count with `--workers auto`
- **Round-robin distribution** — balanced test load across workers

## Quick Start

```bash
# Install
pip install pytest-concurrency

# Run tests with 4 parallel workers
pytest --workers 4

# Auto-detect CPU cores
pytest --workers auto
```

## How It Works

The plugin patches pytest internals (`SetupState`, `FixtureDef`, `os.environ`) to make them thread-local, enabling safe parallel execution. Tests are distributed across workers using a round-robin algorithm, with parametrized tests kept together to avoid setup/teardown conflicts.

## License

MIT