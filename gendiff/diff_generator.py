import json


def generate_diff(first_file: str, second_file: str) -> str:
    """Returns a change in the content in the second file relative to the first

    Args:
        first_file: Path to the first file.
        second_file: Path to the second file.

    Returns:
        A string containing the difference between files.
    """
    with open(first_file) as first_json_file:
        first_file_dict = json.load(first_json_file)

    with open(second_file) as second_json_file:
        second_file_dict = json.load(second_json_file)

    result_dict = {}

    for key, value in first_file_dict.items():
        if key in second_file_dict:
            if value == second_file_dict[key]:
                key = f'  {key}'
                result_dict[key] = value
            else:
                second_value = second_file_dict[key]
                key = f'- {key}'
                result_dict[key] = value
                key = f'+ {key[2:]}'
                result_dict[key] = second_value
        else:
            key = f'- {key}'
            result_dict[key] = value

    for key, value in second_file_dict.items():
        if key in first_file_dict:
            continue
        else:
            key = f'+ {key}'
            result_dict[key] = value

    result_dict = dict(sorted(result_dict.items(), key=lambda item: item[0][2]))

    result = json.dumps(result_dict, indent=2).replace('"', '').replace(',', '')

    return result
