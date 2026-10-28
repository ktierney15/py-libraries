# py-libraries

Personal Python libraries, one uv project per directory.

| Library | Description |
| --- | --- |
| [kt-semver](kt-semver) | Semantic version bumping for CI pipelines |

## Installing

These aren't published to a package index. Install from git with a per-library tag (`<library>-v<version>`):

```bash
uv add "<library> @ git+https://github.com/ktierney15/py-libraries.git@<library>-v<version>#subdirectory=<library>"
```

Or run a library's CLI without installing it:

```bash
uvx --from "git+https://github.com/ktierney15/py-libraries.git@<library>-v<version>#subdirectory=<library>" <command>
```

## Adding a library

```bash
uv init --lib --no-workspace <library>
```

Then add it to the table above and to the test matrix in `.github/workflows/test.yml`.
