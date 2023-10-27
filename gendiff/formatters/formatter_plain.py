from gendiff.diff import is_dict
from typing import Any, Union, Callable


def get_correct_str(value: Any) -> str:
    """Returns the value as a string in the correct form,
            typical for json files.

    Args:
        value: A data.

    Returns:
        A data string in the correct form.
    """

    python_to_json_literals = {
        "True": "true",
        "False": "false",
        "None": "null"
    }

    if str(value) in python_to_json_literals:
        return python_to_json_literals[str(value)]
    else:
        return repr(value)


def get_correct_value(value: Any | dict[str, Any]) -> Union[str, Callable[[Any], str]]:  # noqa: E501
    """Returns the value as a string in the correct form.

    Args:
        value: A data.

    Returns:
        A data string.
    """
    if is_dict(value):
        return '[complex value]'
    else:
        return get_correct_str(value)


def format_diff_plain(diff: dict[str, Any]) -> str:
    """Returns a plain stylized representation of changes in
        the contents of the second file relative to the first.

    Args:
        diff: The dictionary with keys and their description.

    Returns:
        A string containing the difference between files.
    """

    lines = []

    def walk(current_value, path=''):

        for key in current_value.keys():
            status = current_value[key]['status']
            match status:
                case 'added':
                    value = current_value[key]['value']
                    result_value = get_correct_value(value)

                    string = (f'Property \'{path}{key}\' was added with value: '
                              f'{result_value}\n')
                    lines.append(string)

                case 'deleted':
                    string = f'Property \'{path}{key}\' was removed\n'
                    lines.append(string)

                case 'changed':
                    old_value = current_value[key]['old_value']
                    old_result_value = get_correct_value(old_value)

                    new_value = current_value[key]['new_value']
                    new_result_value = get_correct_value(new_value)

                    string = (f'Property \'{path}{key}\' was updated. '
                              f'From {old_result_value} '
                              f'to {new_result_value}\n')
                    lines.append(string)

                case 'unchanged':
                    continue

                case 'nested':
                    value = current_value[key]['children']

                    walk(value, path + f'{key}.')

        result_string = ''.join(lines).strip('\n')

        return result_string

    return walk(diff, '')
