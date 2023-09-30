import os
import pytest
from gendiff.diff_generator import generate_diff


test_directory_path = './tests/fixtures'

first_file_path = os.path.join(test_directory_path, 'file1.json')
second_file_path = os.path.join(test_directory_path, 'file2.json')
result_file_path = os.path.join(test_directory_path, 'result.txt')


@pytest.fixture
def result():
    with open(result_file_path) as result:
        result_list = result.readlines()
        result_string = ''.join(result_list )

        return result_string


def test_generate_diff(result):
    assert generate_diff(first_file_path, second_file_path) == result
