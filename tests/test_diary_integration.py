"""
Docstring for Exercise.tests.test_diary_integration
"""
from lib.diary import *
from lib.diary_entry import *
import pytest

example_contents_3_to_100 = "3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100"
example_contents_3_to_150 = "3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150"
example_contents_3_to_200 = "3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200"

"""
Given a diary entry
Diary returns a list containing a single entry
"""

def test_Diary_returns_single_diary_title_when_single_entry_added():
    diary = Diary()
    diary_entry = DiaryEntry("title 1", "contents 1")
    diary.add(diary_entry)
    actual = diary.all()
    expected = ["title 1"]
    assert actual == expected


"""
Given two diary entries
Diary returns a list containing the titels of two entries
"""

def test_Diary_returns_two_diary_titles_when_two_entries_added():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", "contents 1")
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", "contents 2")
    diary.add(diary_entry2)
    actual = diary.all()
    expected = ["title 1", "title 2"]
    assert actual == expected

# Shall we check contents?

"""
Given two diary entries
Diart returns an integer representing
the number of words in all diary entries
"""

def test_Diary_returns_int_of_total_num_of_words_when_two_entries_added():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", "contents 1")
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", "contents 2")
    diary.add(diary_entry2)
    actual = diary.count_words()
    expected = 8
    assert actual == expected

"""
Given two diary entries
Diary returns an integer representing
the number of words in all diary entries
"""

def test_Diary_returns_int_of_total_num_of_words_when_two_entries_added_with_longer_contents():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", "contents longer 1")
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", "contents longer 2")
    diary.add(diary_entry2)
    actual = diary.count_words()
    expected = 10
    assert actual == expected

"""
Given the number of words the user can read per minute and two lengthy diary entries
Return an int representing the number of minutes required to read
"""

def test_Diary_returns_int_of_total_time_required_to_read_all_entries_for_two_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", example_contents_3_to_200)
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", example_contents_3_to_200)
    diary.add(diary_entry2)
    actual = diary.reading_time(200)
    expected = 2
    assert actual == expected

"""
Given the number of words the user can read per minute and two lengthy diary entries
Return an int representing the number of minutes required to read
"""

def test_Diary_returns_int_of_total_time_required_to_read_all_entries_for_two_entries_using_factor_of_three():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", example_contents_3_to_200)
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", example_contents_3_to_200)
    diary.add(diary_entry2)
    actual = diary.reading_time(66)
    expected = 6
    assert actual == expected

"""
Given the number of words the user can read per minute and three lengthy diary entries
Return the longest diary entry title readable in the specified number of minutes
"""

def test_diary_returns_150_word_length_entry_for_80_wpm_2_min():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", example_contents_3_to_100)
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", example_contents_3_to_150)
    diary.add(diary_entry2)
    diary_entry3 = DiaryEntry("title 3", example_contents_3_to_200)
    diary.add(diary_entry3)
    actual = diary.find_best_entry_for_reading_time(80, 2)
    expected = "title 2"
    assert actual == expected

"""
Given the number of words the user can read per minute and three lengthy diary
entries using differing wpm and minute values
Return the longest diary entry title readable in the specified number of minutes
"""

def test_Diary_returns_longest_entry_that_can_be_read_in_one_minute():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", example_contents_3_to_200)
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", example_contents_3_to_150)
    diary.add(diary_entry2)
    diary_entry3 = DiaryEntry("title 3", example_contents_3_to_100)
    diary.add(diary_entry3)
    actual = diary.find_best_entry_for_reading_time(150, 1)
    expected = "title 2"
    assert actual == expected

"""
Given the number of words the user can read per minute and three lengthy diary entries
Return the longest diary entry title readable in the specified number of minutes
with a different final sort position
"""

def test_diary_returns_150_word_length_entry_for_80_wpm_2_min_using_first_entry():
    diary = Diary()
    diary_entry1 = DiaryEntry("title 1", example_contents_3_to_150)
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("title 2", example_contents_3_to_100)
    diary.add(diary_entry2)
    diary_entry3 = DiaryEntry("title 3", example_contents_3_to_200)
    diary.add(diary_entry3)
    actual = diary.find_best_entry_for_reading_time(80, 2)
    expected = "title 1"
    assert actual == expected