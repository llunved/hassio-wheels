"""Some utils for builder."""
from pathlib import Path
import os
import re

import requests

RE_WHEEL_PLATFORM = re.compile(r"^(?P<name>.*-)cp\d{2}m-linux_\w+\.whl$")


def get_os_release() -> Dict[str, int]:
    """Parse /etc/os_release."""
    with open("/etc/os-release") as f:
        os_release = {}
        for line in f:
            k,v = line.rstrip().split("=")
            # .strip('"') will remove if there or else do nothing
            os_release[k] = v.strip('"') 
            
    return os_release


def os_version() -> str:
    """Return os version for index server."""
    os_release=get_os_release()           
    return f"{os_release['ID']-{os_release['VERSION_ID']}"


def build_arch() -> str:
    """Return build arch for wheels."""
    return os.environ["ARCH"]


def check_url(url: str) -> None:
    """Check if url is responsible."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()


def fix_wheels_name(wheels_folder: Path) -> None:
    """Remove platform tag from filename."""
    for package in wheels_folder.glob("*.whl"):
        match = RE_WHEEL_PLATFORM.match(package.name)
        if not match:
            continue
        package.rename(Path(package.parent, f"{match.group('name')}none-any.whl"))
