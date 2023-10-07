from typing import Any


def is_dict(value: Any) -> bool:
    """Checks whether the passed value is a dictionary.

    Args:
        value: value of any type.

    Returns:
        True if the passed value is a dictionary, False otherwise.
    """

    return isinstance(value, dict)


def make_diff(first_file_dict: dict, second_file_dict: dict) -> dict:
    """Returns a dictionary with a description of each key
            from the passed dictionaries.

    Args:
        first_dict: The contents of the first file
            in the form of a dictionary.
        second_dict: The contents of the second file
            in the form of a dictionary.

    Returns:
        Dictionary with keys and their description.
    """

    keys = sorted(set(first_file_dict.keys()) | set(second_file_dict.keys()))

    result_dict = {}

    for key in keys:
        first_value = first_file_dict.get(key)
        second_value = second_file_dict.get(key)

        if key not in first_file_dict:
            result_dict[key] = {
                'status': 'added',
                'value': second_value
            }

        elif key not in second_file_dict:
            result_dict[key] = {
                'status': 'deleted',
                'value': first_value
            }

        elif is_dict(first_value) and is_dict(second_value):
            result_dict[key] = {
                'status': 'nested',
                'value': make_diff(first_value,
                                   second_value)
            }

        elif first_value != second_value:
            result_dict[key] = {
                'status': 'changed',
                'old_value': first_value,
                'new_value': second_value
            }

        else:
            result_dict[key] = {
                'status': 'unchanged',
                'value': first_value,
            }

    return result_dict
