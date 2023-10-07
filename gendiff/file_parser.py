import json
import yaml


def get_file_format(file_path: str) -> str:
    """Returns the file format.

    Args:
        file_path: Path to the file.

    Returns:
        str: A string with the file format.
    """

    if file_path.endswith('.json'):
        return 'json'
    elif file_path.endswith('.yaml') or file_path.endswith('yml'):
        return 'yaml'


def get_file_content(file_path: str) -> dict:
    """Returns the contents of the file with the extension .json or
            .yaml (.yml) as a dictionary.

    Args:
        file_path: Path to the file.

    Returns:
        A dictionary with file contents.
    """

    file_format = get_file_format(file_path)

    if file_format == 'json':
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

    elif file_format == 'yaml':
        with open(file_path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)
