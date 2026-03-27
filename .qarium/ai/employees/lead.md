# Lead

## Config

| Key            | Value | Description                                  |
|----------------|-------|----------------------------------------------|
| default_branch | main  | Default branch for CI triggers and diff base |

## Architecture & Decisions
- **Thread-local monkey-patching for concurrency** — patches pytest internals (SetupState, FixtureDef) and os.environ to be thread-local, enabling parallel test execution without state collisions
- **Round-robin test distribution** — tests are sorted by nodeid and distributed across workers in round-robin fashion to balance load
- **Test case merging by unique key** — parametrized tests with same module.class.function are grouped and executed together to maintain fixture sharing semantics
- **Conditional plugin activation** — patches only apply when `--workers` flag or `PYTEST_CONCURRENCY_WORKERS` env var is present, avoiding overhead for normal pytest runs
- **Optional allure integration** — allure patching is guarded by ImportError, providing thread-safe allure reporting when the package is installed

## Project Structure
- **Plugin entry in `__init__.py`** — pytest hooks (`pytest_addoption`, `pytest_configure`, `pytest_runtestloop`) defined at package root for entry point discovery
- **Patching modules separated by concern** — `system.py` for os.environ, `fixtures.py` for FixtureDef, `allure.py` for allure — each patch is isolated for maintainability
- **Constants in `envvars.py`** — environment variable names centralized for consistent reference

## Code Patterns
- **`typing as t` import convention** — consistent use of `import typing as t` with `t.Final`, `t.Any`, `t.Optional`, etc.
- **`t.Final` for module constants** — all constants use `t.Final` type hint (e.g., `PYTEST_CONCURRENCY_WORKERS: t.Final`)
- **`@t.final` decorator for classes** — classes not meant for inheritance use the final decorator
- **Private helpers with underscore prefix** — internal functions like `_get_next_item`, `_run_item`, `_create_test_cases`
- **Pylint disable comments inline** — `# pylint: disable=invalid-name` used where needed (e.g., accessing internal `_Environ`)

## TODO
<!-- empty -->

## LLM Directives
<!-- empty -->

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|