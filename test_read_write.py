from read_and_write_csv import *

def test_read_no_file():
    actual = csv_read("fake_file.csv")
    expected = "No file found."
    assert actual == expected

def test_read():
    actual = csv_read("empty.csv")
    expected = []
    assert actual == expected