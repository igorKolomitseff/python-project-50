import json
import yaml
import sys


sys.tracebacklimit = 0


def get_file_format(file_path: str) -> str:
    """Returns the file format.

    Args:
        file_path: Path to the file.

    Returns:
        str: A string with the file format.
    """

    file_format = file_path.split('.')[-1]

    return file_format


def get_file_content(file_path: str) -> dict:
    """Returns the contents of the file with the extension .json or
            .yaml (.yml) as a dictionary.

    Args:
        file_path: Path to the file.

    Returns:
        A dictionary with file contents.
    """

    file_format = get_file_format(file_path)

    match file_format:
        case 'json':
            try:
                with open(file_path, 'r') as json_file:
                    return json.load(json_file)
            except FileNotFoundError:
                raise

        case 'yaml' | 'yml':
            try:
                with open(file_path, 'r') as yaml_file:
                    return yaml.safe_load(yaml_file)
            except FileNotFoundError:
                raise

        case _:
            raise ValueError(f'Unsupported file format: {file_format}')
