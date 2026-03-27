## Config

| Setting          | Value                                             |
|------------------|---------------------------------------------------|
| run_tests_cmd    | `pytest --tb=short`                               |
| lint_cmd         | `ruff check pytest_concurrency/ tests/`           |
| lint_fix_cmd     | `ruff check --fix pytest_concurrency/ tests/`    |
| format_cmd       | `ruff format --check pytest_concurrency/ tests/` |
| format_fix_cmd   | `ruff format pytest_concurrency/ tests/`        |

## Rules

Project test configuration. Used by the `qarium:employees:qa:feature` skill.

### Mapping

| Source path pattern         | Test directory        | Notes            |
|-----------------------------|-----------------------|------------------|
| `pytest_concurrency/**/*.py` | `tests/`               | Flat test layout |

### Mock Patterns

| Pattern | Example |
|---------|---------|
| Mock config object | `config = Mock(); config.getoption.return_value = value` |

### Helpers

| Helper | Location | Purpose |
|--------|----------|---------|
| monkeypatch | tests/conftest.py | Patch os.cpu_count for testing |

### Conventions
- Naming: `test_<what>_<scenario>` (e.g., `test_returns_integer_value_from_config`)
- Test classes: `Test<Subject>` (e.g., `TestGetWorkersCount`)
- Imports: absolute imports from `pytest_concurrency` and `unittest.mock`

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|