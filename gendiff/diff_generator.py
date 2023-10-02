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


def get_correct_value(value: str) -> str:
    """Returns the value in the correct form.

    Args:
        value: A data string.

    Returns:
        str: A data string in the correct form.
    """

    python_to_json_literals = {
        "True": "true",
        "False": "false",
        "None": "null"
    }

    if str(value) in python_to_json_literals:
        return python_to_json_literals[str(value)]
    else:
        return str(value)


def generate_diff(first_file_path: str,  second_file_path: str) -> str:
    """Returns a change in the content in the second file relative to the first.

    Args:
        first_file_path: Path to the first file.
        second_file_path: Path to the second file.

    Returns:
        A string containing the difference between files.
    """

    first_file_dict = get_file_content(first_file_path)
    second_file_dict = get_file_content(second_file_path)

    keys = set(first_file_dict.keys()) | set(second_file_dict.keys())

    result = []

    for key in keys:
        first_value = get_correct_value(first_file_dict.get(key))
        second_value = get_correct_value(second_file_dict.get(key))

        if key not in first_file_dict:
            new_string = f'  + {key}: {second_value}\n'
            result.append(new_string)
        elif key not in second_file_dict:
            new_string = f'  - {key}: {first_value}\n'
            result.append(new_string)
        elif first_value != second_value:
            first_new_string = f'  - {key}: {first_value}\n'
            second_new_string = f'  + {key}: {second_value}\n'
            result.append(first_new_string)
            result.append(second_new_string)
        else:
            new_string = f'    {key}: {first_value}\n'
            result.append(new_string)

    result = sorted(result, key=lambda item: item.lstrip(' -+')[0])

    result_string = ('{\n'
                     + ''.join(result)
                     + '}')

    return result_string
