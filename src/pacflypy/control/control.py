from ..exceptions import ControlFileInvalid

_essential = [
    "Package",
    "Version",
    "Maintainer",
    "Architecture",
    "Description",
    "Section",
    "Priority"
]

_optional = [
    "Vendor",
    "Homepage",
    "Depends",
    "Conflicts",
    "Replaces",
    "Provides",
    "Installed-Size",
    "Pre-Depends",
    "Post-Depends",
    "Recommends",
    "Suggests",
    "Enhances",
    "Breaks",
    "Replaces",
    "Provides",
    "Depends",
    "Conflicts",
    "Replaces",
    "Provides",
]

def load(file) -> dict:
    """
    Load Data from control File and Return Dictionary
    """
    data = file.read()
    string = {}
    for line in data.split("\n"):
        if line:
            key, value = line.split(': ', 1)
            string[key] = value
    return string

def dump(data: dict, file) -> None:
    """
    
    """
    for key, value in data.items():
        file.write(f"{key}: {value}\n")

def check(file_path: str) -> bool:
    """
    Check if Control File Valid
    """
    with open(file_path, "r") as file:
        data = load(file=file)
        for key, value in data.items():
            if key not in _essential and key not in _optional:
                raise ControlFileInvalid(file_path, f"Invalid Key: {key}")
            elif key in _essential and not value:
                raise ControlFileInvalid(file_path, f"Essential Key: {key} is Empty")
            elif key in _optional and not value:
                raise ControlFileInvalid(file_path, f"Optional Key: {key} is Empty")
    return True

