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