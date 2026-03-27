## Config

| Key            | Value   | Description                                  |
|----------------|---------|----------------------------------------------|
| ci_provider    | github  | CI/CD platform                               |
| trigger_branch | main    | Default branch for CI triggers and diff base |

## Rules

### Workflow Registry

| Workflow | File          | Trigger               | Purpose                                |
|----------|---------------|-----------------------|----------------------------------------|
| tests    | `tests.yml`   | push/PR to main       | Run pytest across Python 3.10-3.13    |
| lint     | `lint.yml`    | push/PR to main       | Ruff lint and format check             |
| docs     | `docs.yml`    | push/PR to main       | Build docs with mkdocs                 |
| publish  | `publish.yml` | tags v*               | Build and publish package to PyPI      |

### Conventions

- Python version in CI jobs: 3.12 (lint, docs, publish)
- Test matrix covers all supported versions: 3.10, 3.11, 3.12, 3.13
- Actions pinned to major version: @v4, @v5

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|