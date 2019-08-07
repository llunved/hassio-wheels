"""Install RPMs for build on host system."""
import subprocess
import sys


def install_dnf(rpms: str) -> None:
    """Install all RPMs string formated as 'package1;package2'."""
    packages = " ".join(rpmss.split(";"))

    result = subprocess.run(
        f"dnf install -y {packages}",
        shell=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )

    # Check result of program
    result.check_returncode()
