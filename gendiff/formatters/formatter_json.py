import json


def format_diff_json(diff: dict) -> str:
    """Returns a json representation of changes in
        the contents of the second file relative to the first.

    Args:
        diff: The dictionary with keys and their description.

    Returns:
        A string containing the difference between files.
    """

    result = json.dumps(diff, indent=4)

    return result
