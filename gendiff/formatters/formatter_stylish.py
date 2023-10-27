from gendiff.diff import is_dict
from typing import Any

REPLACER = ' '
SPACES_COUNT = 4
LEFT_OFFSET = 2
STATUS_DICT = {
    'added': '+ ',
    'deleted': '- ',
    'nested': '  ',
    'changed': {
        'old': '- ',
        'new': '+ '
    },
    'unchanged': '  '
}


def get_correct_str(value: Any) -> str:
    """Returns the value as a string in the correct form,
            typical for json files.

    Args:
        value: A data string.

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
        return str(value)


def convert_dict_to_str(value: Any | dict[str, Any], depth: int) -> str:
    """Returns the passed value as a string.
            Special attention is paid to converting
            a nested dictionary into a string.

    Args:
        value: A data.
        depth: Dictionary nesting depth.

    Returns:
        A data string.
    """

    def iter_(current_value, depth):
        if not is_dict(current_value):
            return get_correct_str(current_value)

        deep_indent_size = depth * SPACES_COUNT - LEFT_OFFSET
        current_indent = REPLACER * (deep_indent_size - LEFT_OFFSET)
        deep_indent = REPLACER * (deep_indent_size + LEFT_OFFSET)

        lines = []

        for key, val in current_value.items():
            string = (f'{deep_indent}{key}: {iter_(val, depth+1)}\n')

            lines.append(string)

        result_string = ('{\n'
                         + ''.join(lines)
                         + f'{current_indent}'
                         + '}')

        return result_string

    return iter_(value, depth)


def format_diff_stylish(diff: dict[str, Any]) -> str:
    """Returns a stylized representation of changes in
        the contents of the second file relative to the first.

    Args:
        diff: The dictionary with keys and their description.

    Returns:
        A string containing the difference between files.
    """

    def walk(current_value, depth=1):
        deep_indent_size = depth * SPACES_COUNT - LEFT_OFFSET
        current_indent = REPLACER * (deep_indent_size - LEFT_OFFSET)

        lines = []

        for key in current_value.keys():
            status = current_value[key]['status']
            match status:
                case 'added' | 'deleted' | 'unchanged':
                    deep_indent = (REPLACER
                                   * deep_indent_size
                                   + STATUS_DICT[status])

                    value = current_value[key]['value']
                    result_value = convert_dict_to_str(value, depth + 1)

                    string = f'{deep_indent}{key}: {result_value}\n'

                    lines.append(string)

                case 'nested':
                    deep_indent = (REPLACER
                                   * deep_indent_size
                                   + STATUS_DICT[status])

                    value = current_value[key]['children']

                    string = f'{deep_indent}{key}: {walk(value, depth + 1)}\n'
                    lines.append(string)

                case 'changed':
                    old_deep_indent = (REPLACER
                                       * deep_indent_size
                                       + STATUS_DICT[status]['old'])

                    old_value = current_value[key]['old_value']
                    old_result_value = convert_dict_to_str(old_value, depth + 1)

                    new_deep_indent = (REPLACER
                                       * deep_indent_size
                                       + STATUS_DICT[status]['new'])

                    new_value = current_value[key]['new_value']
                    new_result_value = convert_dict_to_str(new_value, depth + 1)

                    first_string = (f'{old_deep_indent}{key}: '
                                    f'{old_result_value}\n')

                    second_string = (f'{new_deep_indent}{key}: '
                                     f'{new_result_value}\n')

                    lines.append(first_string)
                    lines.append(second_string)

        result_string = ('{\n'
                         + ''.join(lines)
                         + f'{current_indent}'
                         + '}')

        return result_string

    return walk(diff)
