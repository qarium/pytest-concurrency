# DevOps Config

## Config

| Key            | Value          | Description                                  |
|----------------|----------------|----------------------------------------------|
| ci_provider    | github-actions | CI provider                                  |
| trigger_branch | 0.0.x          | Default branch for CI triggers and diff base |
| diff_range     | HEAD~5         | Git diff range for auto-analysis in feature  |

## Rules

### Workflow Registry

| Workflow | File                            | Trigger                     | Purpose             |
|----------|--------------------------------|-----------------------------|---------------------|
| tests       | `.github/workflows/tests.yml`       | push/PR to 0.0.x  | pytest matrix (caller)        |
| lint        | `.github/workflows/lint.yml`        | push/PR to 0.0.x  | ruff check + format           |
| docs        | `.github/workflows/docs.yml`        | push to 0.0.x     | mkdocs deploy                 |
| publish     | `.github/workflows/publish.yml`     | workflow_dispatch  | PyPI release (caller)         |
| new_version | `.github/workflows/new_version.yml` | workflow_dispatch  | Create version branch (caller)|
| strictacode | `.github/workflows/strictacode.yml` | push/PR to 0.0.x  | strictacode analysis          |
| notify      | `.github/workflows/notify.yml`      | workflow_run: Publish Release | Telegram notify on release (caller) |

### Conventions

- Python versions in CI matrix sync with pyproject.toml `classifiers`
- Lint uses `astral-sh/ruff-action` for ruff lint
- Format check uses `ruff format --check pytest_concurrency/ tests/`
- Tests, publish, new_version are callers of `qarium/ci` reusable workflows

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
