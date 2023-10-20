import os
import pytest
import json
import yaml
from gendiff.file_parser import get_file_content


test_directory_path = './tests/fixtures'

right_file_name = 'file1_nested'
wrong_file_name = 'file_nested'

json_file_format = '.json'
yaml_file_format = '.yml'

wrong_file_format = 'txt'


right_json_file_path = os.path.join(test_directory_path,
                                    (right_file_name
                                     + json_file_format))

right_yaml_file_path = os.path.join(test_directory_path,
                                    (right_file_name
                                     + yaml_file_format))

wrong_json_file_path = os.path.join(test_directory_path,
                                    (wrong_file_name
                                     + json_file_format))

wrong_yaml_file_path = os.path.join(test_directory_path,
                                    (wrong_file_name
                                     + yaml_file_format))

unsupported_file_format_file_path = os.path.join(test_directory_path,
                                                 (right_file_name
                                                  + wrong_file_format))


@pytest.fixture
def json_file_content():
    with open(right_json_file_path, 'r') as json_file:
        return json.load(json_file)


@pytest.fixture
def yaml_file_content():
    with open(right_yaml_file_path, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)


def test_get_file_content_json_file(json_file_content):
    result = json_file_content
    assert get_file_content(right_json_file_path) == result

    with pytest.raises(FileNotFoundError):
        get_file_content(wrong_json_file_path)


def test_get_file_content_yaml_file(yaml_file_content):
    result = yaml_file_content
    assert get_file_content(right_yaml_file_path) == result

    with pytest.raises(FileNotFoundError):
        get_file_content(wrong_yaml_file_path)


def test_get_file_content_unsupported_file_format():
    with pytest.raises(ValueError):
        get_file_content(unsupported_file_format_file_path)
