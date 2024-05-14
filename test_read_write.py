from read_and_write_csv import *

def test_read_no_file():
    actual = csv_read("fake_file.csv")
    expected = "No file found."
    assert actual == expected

def test_read():
    actual = csv_read("empty.csv")
    expected = []
    assert actual == expected

def test_write():
    actual = write_to_new("Small_lil_file.csv", [0], "less_empty.csv")
    expected = [['column 1']]
    assert actual == expected

def test_write_bad():
    actual = write_to_new("Bad_test.csv", [], "missing.csv")
    expected = "Invalid csv!"
    assert actual == expected