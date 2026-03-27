# DevOps Config

## Config

| Key            | Value          | Description                                  |
|----------------|----------------|----------------------------------------------|
| ci_provider    | github-actions | CI provider                                  |
| trigger_branch | master         | Default branch for CI triggers and diff base |
| diff_range     | HEAD~5         | Git diff range for auto-analysis in feature  |

## Rules

### Workflow Registry

| Workflow | File                            | Trigger                     | Purpose             |
|----------|--------------------------------|-----------------------------|---------------------|
| tests    | `.github/workflows/tests.yml`   | push/PR to master            | pytest matrix        |
| lint     | `.github/workflows/lint.yml`    | push/PR to master            | ruff check + format |
| docs     | `.github/workflows/docs.yml`    | push to master               | mkdocs deploy        |
| publish  | `.github/workflows/publish.yml` | tag v*                       | PyPI release         |

### Conventions

- Python versions in CI matrix sync with pyproject.toml `classifiers`
- Lint uses `astral-sh/ruff-action` for ruff lint
- Format check uses `ruff format --check pytest_concurrency/ tests/`
- Tests use `pytest --tb=short` with matrix strategy

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
