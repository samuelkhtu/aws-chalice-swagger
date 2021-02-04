from chalicelib.utils.file_utils import find_file, get_static_file
import pytest
import os


def test_find_file():
    target_file = "swagger-ui.css"
    path = find_file(target_file)
    result_file = os.path.basename(path)
    assert result_file == target_file


def test_find_file_expect_fail():
    target_file = "file_not_exist"
    with pytest.raises(FileNotFoundError):
        path = find_file(target_file)


def test_read_file_expect_pass():
    file_content = None
    # read content directly from file
    with open(find_file("swagger-ui.css"), "r") as f:
        file_content = f.read()
        # print(file_content)
    # get static file content =
    target_content = get_static_file("swagger-ui.css")
    # print(target_content)
    assert file_content == target_content


def test_read_file_expect_exception():
    with pytest.raises(FileNotFoundError):
        target_content = get_static_file("file_not_exist")


def test_read_file_empty():
    with pytest.raises(ValueError):
        get_static_file(file_name="empty_file.json", search_from_base_path=os.getcwd())
        # print(target_content)
