from lib.diary import *

"""
Upon instantiation
Diary creates an empty dictionary
"""

def test_Diary_returns_empty_dictionary():
    diary = Diary()
    actual = diary._list_of_entries
    expected = []
    assert actual == expected