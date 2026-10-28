"""
Author: Kevin Tierney
Description: Semantic versioning for release tags.

examples:
    create_new_version('patch', 'v1.2.1') -> 'v1.2.2'
    create_new_version('minor', 'v1.2.1') -> 'v1.3.0'
    create_new_version('major', 'v1.2.1') -> 'v2.0.0'
"""

BUMP_TYPES = ("major", "minor", "patch")


def create_new_version(version_type: str, current_version: str) -> str:
    version_type = version_type.lower()
    if version_type not in BUMP_TYPES:
        raise ValueError(f"version_type must be one of {BUMP_TYPES}, got {version_type!r}")

    current_version = current_version.strip()
    prefix = ""
    if current_version[:1].lower() == "v":
        prefix = current_version[0]
        current_version = current_version[1:]

    version_split = current_version.split(".")
    if len(version_split) != 3 or not all(part.isdigit() for part in version_split):
        raise ValueError(f"current_version must look like 'v1.2.3' or '1.2.3', got {prefix + current_version!r}")

    major, minor, patch = (int(part) for part in version_split)

    if version_type == "major":
        major, minor, patch = major + 1, 0, 0
    elif version_type == "minor":
        minor, patch = minor + 1, 0
    elif version_type == "patch":
        patch += 1

    return f"{prefix}{major}.{minor}.{patch}"


def bump_type_from_message(message: str, default: str = "minor") -> str:
    """Pick a bump type from a commit message containing PATCH or MAJOR, else ``default``."""
    if "PATCH" in message:
        return "patch"
    if "MAJOR" in message:
        return "major"
    return default
