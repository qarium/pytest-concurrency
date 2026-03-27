# Tech Writer Config

## Config

| Key           | Value                      | Description                         |
|---------------|----------------------------|-------------------------------------|
| build_cmd     | `mkdocs build`             | Build validation command            |
| deploy_cmd    | `mkdocs gh-deploy --force` | Deploy command                      |
| examples_file | `docs/examples.md`         | File for usage examples             |
| logo_url      | `https://avatars.githubusercontent.com/u/262344922?s=200&v=4` | Standard qarium logo |
| base_branch   | `master`                   | Base branch for git diff comparison |

## Rules

### Mapping

| Source path | Documentation files |
|-------------|---------------------|
| `pytest_concurrency/tools.py` | `docs/api-reference.md` (get_workers_count) |
| `pytest_concurrency/__init__.py` | `docs/getting-started.md`, `docs/configuration.md` |
| `pytest_concurrency/envvars.py` | `docs/configuration.md` (env vars section) |

### Conventions

- Use `#` for page titles (H1)
- Use `##` for major sections
- Use `###` for subsections
- Include code examples in Python and Bash blocks
- Link to external docs with full URLs

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
