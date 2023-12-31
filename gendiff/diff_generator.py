from gendiff.file_parser import get_file_content
from gendiff.diff import make_diff
from gendiff.formatters.formatter_stylish import format_diff_stylish
from gendiff.formatters.formatter_plain import format_diff_plain
from gendiff.formatters.formatter_json import format_diff_json
from typing import Callable, Any


def get_formatter(formatter: str) -> Callable[[dict[str, Any]], str]:
    """Returns the formatter function.

    Args:
        formatter: Name of the formatter.

    Returns:
        The formatter function.
    """

    match formatter:
        case 'stylish':
            return format_diff_stylish
        case 'plain':
            return format_diff_plain
        case 'json':
            return format_diff_json


def generate_diff(first_file_path: str,
                  second_file_path: str,
                  formatter: str = 'stylish') -> str:
    """Returns a change in the content in the second file relative to the first.

    Args:
        first_file_path: Path to the first file.
        second_file_path: Path to the second file.
        formatter (optional): Nested dictionary formatter.
            Defaults to 'stylish'.

    Returns:
        A string containing the difference between files.
    """

    first_file_dict = get_file_content(first_file_path)
    second_file_dict = get_file_content(second_file_path)

    format_diff = get_formatter(formatter)

    diff_dict = make_diff(first_file_dict, second_file_dict)

    result_string = format_diff(diff_dict)

    return result_string
