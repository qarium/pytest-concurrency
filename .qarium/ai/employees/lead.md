# Lead

## Config

| Key            | Value  | Description                                  |
|----------------|--------|----------------------------------------------|
| default_branch | master | Default branch for CI triggers and diff base |

## Architecture & Decisions
- **Monkey patching pytest internals for thread-safety** — plugin modifies `_pytest.runner.SetupState`, `_pytest.fixtures.FixtureDef`, and `os._Environ` to make them thread-local, enabling parallel test execution
- **threading.local inheritance pattern** — classes inherit from both `threading.local` and target class to achieve thread-isolated state without changing pytest's architecture
- **Optional Allure integration via ImportError handling** — allure support is optional; if not installed, patch function becomes a no-op
- **Round-robin test distribution** — tests are distributed across workers using round-robin algorithm for balanced load
- **Test case merging by unique key** — parametrized tests with same module.class.function are kept together to avoid setup/teardown conflicts

## Project Structure
- **Plugin entry point with conditional patching** — main module contains pytest hooks and applies patches only when plugin is enabled via CLI/env
- **Patching logic separated by concern** — one module per subsystem (os environ, fixtures, runner, allure integration)
- **Entry point via pytest11 hook** — standard pytest plugin discovery mechanism

## Code Patterns
- **@t.final decorator on thread-local classes** — prevents inheritance of classes designed for thread-local patching
- **t.Final for constants** — module-level constants use typing.Final for clarity
- **Intentional private attribute access with # noqa: B009** — accessing pytest/os internals requires pylint disable with explanatory comment
- **Absolute imports with explicit module paths** — `from _pytest.config import Config` style for clarity
- **Optional dependencies wrapped in try/except ImportError** — graceful degradation when optional packages (allure) are missing

## TODO
<!-- empty -->

## LLM Directives
<!-- empty -->

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
| `git symbolic-ref` returns stale branch name | Local `refs/remotes/origin/HEAD` symlink not updated after branch rename | Verify with `git remote show origin \| grep "HEAD branch"` or `git ls-remote --exit-code` |