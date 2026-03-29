""" Homework 8 task 7 Tests"""


import pytest
from hw_8_7 import FileProcessor


def test_file_write_read(tmpdir):
    """Test file write and read"""
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_write_read_empty_string(tmpdir):
    """Test file write and read with empty file"""
    file = tmpdir.join("empty.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)
    assert content == ""


def test_write_read_large_data(tmpdir):
    """Test file write and read with large file"""
    file = tmpdir.join("large.txt")
    large_data = "A" * 10_000  # 10 000 символів
    FileProcessor.write_to_file(file, large_data)
    content = FileProcessor.read_from_file(file)
    assert content == large_data


def test_read_nonexistent_file(tmpdir):
    """Test file read with nonexistent file"""
    file = tmpdir.join("nofile.txt")
    with pytest.raises(FileNotFoundError):
        FileProcessor.read_from_file(file)


@pytest.mark.parametrize(
    "data",
    [
        "Short text",
        "",
        "Line1\nLine2\nLine3",
        "😊" * 100,  # Юнікод
    ]
)
def test_write_read_param(tmpdir, data):
    """Test file write and read with param"""
    file = tmpdir.join("param.txt")
    FileProcessor.write_to_file(file, data)
    content = FileProcessor.read_from_file(file)
    assert content == data
