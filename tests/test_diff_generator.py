import os
import pytest
from gendiff.diff_generator import generate_diff


test_directory_path = './tests/fixtures'

file1_flat_name = 'file1_flat'
file1_nested_name = 'file1_nested'
file2_flat_name = 'file2_flat'
file2_nested_name = 'file2_nested'

json_file_format = '.json'
yaml_file_format = '.yml'

result_flat_file_name = 'result_flat'
result_stylish_file_name = 'result_stylish'
result_plain_file_name = 'result_plain'

result_file_format = '.txt'


first_flat_json_file_path = os.path.join(test_directory_path, file1_flat_name + json_file_format)
second_flat_json_file_path = os.path.join(test_directory_path, file2_flat_name + json_file_format)

first_nested_json_file_path = os.path.join(test_directory_path, file1_nested_name + json_file_format)
second_nested_json_file_path = os.path.join(test_directory_path, file2_nested_name + json_file_format)

first_flat_yaml_file_path = os.path.join(test_directory_path, file1_flat_name + yaml_file_format)
second_flat_yaml_file_path = os.path.join(test_directory_path, file2_flat_name + yaml_file_format)

first_nested_yaml_file_path = os.path.join(test_directory_path, file1_nested_name + yaml_file_format)
second_nested_yaml_file_path = os.path.join(test_directory_path, file2_nested_name + yaml_file_format)


format_diff_stylish = 'stylish'
format_diff_plain = 'plain'


@pytest.fixture
def result_flat():
    result_file_path = os.path.join(test_directory_path, result_flat_file_name + result_file_format)

    with open(result_file_path) as result_flat:
        result_list = result_flat.readlines()
        result_string = ''.join(result_list)

        return result_string


@pytest.fixture
def result_stylish():
    result_file_path = os.path.join(test_directory_path, result_stylish_file_name + result_file_format)

    with open(result_file_path) as result_stylish:
        result_list = result_stylish.readlines()
        result_string = ''.join(result_list)

        return result_string


@pytest.fixture
def result_plain():
    result_file_path = os.path.join(test_directory_path, result_plain_file_name + result_file_format)

    with open(result_file_path) as result_plain:
        result_list = result_plain.readlines()
        result_string = ''.join(result_list)

        return result_string


def test_generate_diff_flat_files(result_flat):
    result = result_flat
    assert generate_diff(first_flat_json_file_path, second_flat_json_file_path) == result 
    assert generate_diff(first_flat_json_file_path, second_flat_yaml_file_path) == result 
    assert generate_diff(first_flat_yaml_file_path, second_flat_json_file_path) == result 
    assert generate_diff(first_flat_yaml_file_path, second_flat_yaml_file_path) == result 


def test_generate_diff_nested_files_stylish(result_stylish):
    result = result_stylish
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path) == result 
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path) == result 
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path) == result 
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path) == result


def test_generate_diff_nested_files_plain(result_plain):
    result = result_plain
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path, format_diff_plain) == result 
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path, format_diff_plain) == result 
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path, format_diff_plain) == result 
    assert generate_diff(first_nested_json_file_path, second_nested_json_file_path, format_diff_plain) == result