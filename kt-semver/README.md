# kt-semver

Semantic version bumping for CI pipelines. Replaces the copy-pasted `sem-ver.py` script.

## Usage in GitHub Actions

No install step needed. `uvx` runs it straight from this repo:

```yaml
- uses: astral-sh/setup-uv@v6

- name: Semantic Versioning
  run: |
    NEW_TAG=$(uvx --from "git+https://github.com/ktierney15/py-libraries.git@kt-semver-v0.1.0#subdirectory=kt-semver" \
      kt-semver --message "${{ env.commit_message }}" "$(git describe --tags --abbrev=0)")
    echo "updated_tag=$NEW_TAG" >> "$GITHUB_ENV"
```

## CLI

```bash
kt-semver patch v1.2.1                       # v1.2.2
kt-semver minor v1.2.1                       # v1.3.0
kt-semver major v1.2.1                       # v2.0.0
kt-semver --message "MAJOR: rework" v1.2.1   # v2.0.0  (PATCH -> patch, MAJOR -> major, else minor)
```

The `v` prefix is kept if present. Invalid input exits with code 2.

## Python

```bash
uv add "kt-semver @ git+https://github.com/ktierney15/py-libraries.git@kt-semver-v0.1.0#subdirectory=kt-semver"
```

```python
from kt_semver import create_new_version, bump_type_from_message

create_new_version("minor", "v1.2.1")       # "v1.3.0"
bump_type_from_message("fix: PATCH typo")   # "patch"
```

## Development

```bash
cd kt-semver
uv run pytest
```
