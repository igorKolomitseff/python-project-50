import os
import pytest
from gendiff.diff_generator import generate_diff


test_directory_path = './tests/fixtures'

test_first_file_name = 'file1'
test_second_file_name = 'file2'

test_json_file_format = '.json'
test_yaml_file_format = '.yml'

test_result_file_name = 'result'
test_result_file_format = '.txt'


first_json_file_path = os.path.join(test_directory_path, test_first_file_name + test_json_file_format)
second_json_file_path = os.path.join(test_directory_path, test_second_file_name + test_json_file_format)

first_yaml_file_path = os.path.join(test_directory_path, test_first_file_name + test_yaml_file_format)
second_yaml_file_path = os.path.join(test_directory_path, test_second_file_name + test_yaml_file_format)


@pytest.fixture
def result():
    result_file_path = os.path.join(test_directory_path, test_result_file_name + test_result_file_format)

    with open(result_file_path) as result:
        result_list = result.readlines()
        result_string = ''.join(result_list)

        return result_string


def test_generate_diff_json_json_files(result):
    assert generate_diff(first_json_file_path, second_json_file_path) == result


def test_generate_diff_json_yaml_files(result):
    assert generate_diff(first_json_file_path, second_yaml_file_path) == result


def test_generate_diff_yaml_json_files(result):
    assert generate_diff(first_yaml_file_path, second_json_file_path) == result


def test_generate_diff_yaml_yaml_files(result):
    assert generate_diff(first_yaml_file_path, second_yaml_file_path) == result