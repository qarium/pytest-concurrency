# Examples

## Basic Parallel Execution

```bash
# Run tests with 4 parallel workers
pytest --workers 4 tests/
```

## Auto-Detect CPU Count

```bash
# Automatically use all available CPUs
pytest --workers auto
```

## Via Environment Variable

```bash
# Set workers via environment (useful for CI)
export PYTEST_CONCURRENCY_WORKERS=4
pytest
```

## With Timeout

```bash
# Fail if workers don't complete in 5 minutes
pytest --workers 4 --worker-timeout 300
```

## CI/CD Integration

### GitHub Actions

```yaml
- name: Run tests
  run: pytest --workers auto --worker-timeout 600
  env:
    PYTEST_CONCURRENCY_WORKERS: ${{ vars.PARALLEL_WORKERS }}
```

### GitLab CI

```yaml
test:
  script:
    - pytest --workers ${CI_PARALLELISM:-auto}
```

## With Coverage

```bash
# Works with pytest-cov
pytest --workers 4 --cov=myapp --cov-report=term-missing
```

## With Allure Reports

```bash
# Install allure-pytest first
pip install allure-pytest pytest-concurrency

# Run with parallel execution and Allure
pytest --workers 4 --alluredir=allure-results
```

::: note
pytest-concurrency automatically patches Allure classes for thread-safety when `allure-pytest` is installed.
:::

## Thread-Safe Test Patterns

### Good: Stateless Tests

```python
def test_pure_function():
    # Pure functions are safe
    result = calculate_something(42)
    assert result == expected_value

def test_with_fixtures(db_session):
    # Fixtures are thread-local when patched
    assert db_session.query(User).count() >= 0
```

### Avoid: Shared Mutable State

```python
# BAD: Shared mutable state
shared_list = []

def test_appends_to_list():
    shared_list.append(1)  # Race condition!
    assert len(shared_list) == 1
```

### Fix: Thread-Local Storage

```python
import threading

# GOOD: Thread-local state
local_data = threading.local()

def test_with_thread_local():
    local_data.value = 42
    assert local_data.value == 42
```