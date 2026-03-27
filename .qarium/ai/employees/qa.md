## Config

| Setting          | Value                                  |
|------------------|----------------------------------------|
| run_tests_cmd    | `pytest --tb=short`                    |
| lint_cmd         | `ruff check pytest_concurrency/ tests/` |
| lint_fix_cmd     | `ruff check --fix pytest_concurrency/ tests/` |
| format_cmd       | `ruff format --check pytest_concurrency/ tests/` |
| format_fix_cmd   | `ruff format pytest_concurrency/ tests/` |

## Rules

Project test configuration. Used by the `qarium:employees:qa:feature` skill.

### Mapping

| Source path pattern         | Test directory       | Notes         |
|------------------------------|-----------------------|---------------|
| `pytest_concurrency/**/*.py` | `tests/`                | Flat layout    |

### Mock Patterns
| Pattern | Example |
|---------|---------|

### Helpers
| Helper | Location | Purpose |
|--------|----------|---------|

### Conventions
- Naming: `test_<what>_<scenario>`
- Never mock `builtins.open` — use `tmp_path` fixture
- Integration tests use `pytest.mark.skipif` when external tools unavailable

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|