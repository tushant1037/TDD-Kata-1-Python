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