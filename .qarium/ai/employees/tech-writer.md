# Tech Writer Config

## Config

| Key           | Value                      | Description                         |
|---------------|----------------------------|-------------------------------------|
| build_cmd     | `mkdocs build`             | Build validation command            |
| deploy_cmd    | `mkdocs gh-deploy --force` | Deploy command                      |
| base_branch   | `main`                   | Base branch for git diff comparison |

## Rules

### Mapping

| Source path                        | Documentation files             |
|-------------------------------------|---------------------------------|
| `pytest_concurrency/__init__.py`      | `docs/api.md`, `docs/usage.md`    |
| `pytest_concurrency/allure.py`        | `docs/usage.md`                 |
| `pytest_concurrency/envvars.py`        | `docs/configuration.md`            |
| `pytest_concurrency/fixtures.py`      | `docs/api.md`                    |
| `pytest_concurrency/runner.py`        | `docs/api.md`, `docs/usage.md`    |
| `pytest_concurrency/system.py`        | `docs/api.md`                    |
| `pytest_concurrency/tools.py`        | `docs/api.md`                    |

### Conventions

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|