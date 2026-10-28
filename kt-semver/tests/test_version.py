import pytest

from kt_semver import bump_type_from_message, create_new_version
from kt_semver.cli import main


@pytest.mark.parametrize(
    ("version_type", "current", "expected"),
    [
        ("patch", "v1.2.1", "v1.2.2"),
        ("minor", "v1.2.1", "v1.3.0"),
        ("major", "v1.2.1", "v2.0.0"),
        ("patch", "1.2.1", "1.2.2"),
        ("minor", "V0.9.9", "V0.10.0"),
        ("MAJOR", " v1.2.3\n", "v2.0.0"),
    ],
)
def test_create_new_version(version_type, current, expected):
    assert create_new_version(version_type, current) == expected


@pytest.mark.parametrize("current", ["", "v", "v1.2", "v1.2.3.4", "v1.x.3", "v1.2.3-rc1"])
def test_create_new_version_rejects_bad_versions(current):
    with pytest.raises(ValueError):
        create_new_version("patch", current)


def test_create_new_version_rejects_bad_type():
    with pytest.raises(ValueError):
        create_new_version("huge", "v1.0.0")


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        ("Merge pull request #4 from x/PATCH-fix", "patch"),
        ("MAJOR: drop python 3.8", "major"),
        ("add feature", "minor"),
        ("PATCH and MAJOR", "patch"),
    ],
)
def test_bump_type_from_message(message, expected):
    assert bump_type_from_message(message) == expected


def test_cli_explicit_type(capsys):
    assert main(["patch", "v1.2.1"]) == 0
    assert capsys.readouterr().out == "v1.2.2\n"


def test_cli_from_message(capsys):
    assert main(["--message", "MAJOR rewrite", "v1.2.1"]) == 0
    assert capsys.readouterr().out == "v2.0.0\n"


@pytest.mark.parametrize("argv", [["huge", "v1.0.0"], ["v1.0.0"], ["patch", "nope"], ["-m", "x", "patch", "v1.0.0"]])
def test_cli_errors(argv):
    with pytest.raises(SystemExit) as exc:
        main(argv)
    assert exc.value.code == 2
