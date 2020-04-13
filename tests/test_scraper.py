import pytest
import ms_corona.scraper as victim


def test_convert_written_number_to_int():
    assert victim.convert_written_out_number("sechs ") == 6
    assert victim.convert_written_out_number("zehn") == "zehn"
    assert victim.convert_written_out_number("5") == "5"


def test_number_in_string_one_number():
    assert victim.number_in_string("Test with 4 numbers") == 4


def test_number_in_string_multiple_numbers():
    assert victim.number_in_string("Test with 2 numbers, 4 apples and nineteen dinos") == 2


def test_number_in_string_written_below_10():
    assert victim.number_in_string("Test with drei numbers, 4 apples and nineteen dinos") == 3


def test_number_in_string_written_above_10():
    assert victim.number_in_string("Test with dreizehn numbers, 4 apples and nineteen dinos") == 4