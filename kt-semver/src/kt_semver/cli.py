"""
Command line entry point.

examples:
    kt-semver patch v1.2.1                  -> v1.2.2
    kt-semver minor v1.2.1                  -> v1.3.0
    kt-semver major v1.2.1                  -> v2.0.0
    kt-semver --message "MAJOR: rework" v1.2.1  -> v2.0.0
    kt-semver --message "fix typo" v1.2.1       -> v1.3.0
"""

import argparse
from typing import List, Optional

from kt_semver.version import BUMP_TYPES, bump_type_from_message, create_new_version


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="kt-semver", description="Arguments needed to version your application")
    parser.add_argument("args", nargs="+", metavar="[version_type] current_version",
                        help="Version type to create (major, minor, or patch) followed by the current version")
    parser.add_argument("-m", "--message",
                        help="Commit message to infer the version type from (PATCH -> patch, MAJOR -> major, else minor)")
    parsed = parser.parse_args(argv)

    if parsed.message is not None:
        if len(parsed.args) != 1:
            parser.error("with --message, pass only the current version")
        version_type, current_version = bump_type_from_message(parsed.message), parsed.args[0]
    else:
        if len(parsed.args) != 2:
            parser.error("pass a version type and the current version, e.g. 'patch v1.2.1'")
        version_type, current_version = parsed.args
        if version_type.lower() not in BUMP_TYPES:
            parser.error(f"version_type must be one of {', '.join(BUMP_TYPES)}")

    try:
        print(create_new_version(version_type, current_version))
    except ValueError as e:
        parser.error(str(e))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
