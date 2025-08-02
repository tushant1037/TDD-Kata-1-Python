import pytest
from string_calculator import StringCalculator

calc = StringCalculator()

def test_empty_string_returns_zero():
    assert calc.Add("") == 0

def test_single_number_returns_value():
    assert calc.Add("1") == 1

def test_two_numbers_returns_sum():
    assert calc.Add("1,2") == 3

def test_multiple_numbers_returns_sum():
    assert calc.Add("1,2,3,4,5") == 15
    assert calc.Add("10,20,30") == 60

def test_newline_and_commas_as_delimiters():
    assert calc.Add("1\n2,3") == 6
    assert calc.Add("4\n5\n6") == 15
    assert calc.Add("7,8\n9") == 24

def test_custom_delimiter_semicolon():
    assert calc.Add("//;\n1;2") == 3

def test_custom_delimiter_pipe():
    assert calc.Add("//|\n4|5|6") == 15

def test_custom_delimiter_works_with_single_number():
    assert calc.Add("//.\n9") == 9

def test_negative_number_raises_exception():
    with pytest.raises(ValueError, match="negatives not allowed: -1"):
        calc.Add("1,-1")

def test_multiple_negatives_raise_exception_with_all_listed():
    with pytest.raises(ValueError, match="negatives not allowed: -1, -4"):
        calc.Add("1,-1,2,-4,5")

def test_numbers_greater_than_1000_are_ignored():
    assert calc.Add("2,1001") == 2
    assert calc.Add("1000,1001,1002,3") == 1003
    assert calc.Add("//;\n1001;1002;1") == 1