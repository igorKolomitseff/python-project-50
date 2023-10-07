from gendiff.file_parser import get_file_content
from gendiff.diff import make_diff
from gendiff.formatter_stylish import format_diff


def generate_diff(first_file_path: str,
                  second_file_path: str,
                  formatter='stylish') -> str:
    """Returns a change in the content in the second file relative to the first.

    Args:
        first_file_path: Path to the first file.
        second_file_path: Path to the second file.
        formatter (optional): Nested dictionary formatter.
            Defaults to 'stylish'.

    Returns:
        str:A string containing the difference between files.
    """

    first_file_dict = get_file_content(first_file_path)
    second_file_dict = get_file_content(second_file_path)

    diff_dict = make_diff(first_file_dict, second_file_dict)

    result_string = format_diff(diff_dict)

    return result_string
