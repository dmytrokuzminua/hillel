""" Homework 8 task 9 Tests"""


import pytest
from hw_8_9 import AgeVerifier


@pytest.mark.parametrize(
    "age, expected",
    [
        (0, False),
        (17, False),
        (18, True),
        (30, True),
        (120, True),
    ]
)
def test_is_adult_param(age, expected):
    """Testing for all ages"""
    assert AgeVerifier.is_adult(age) == expected


@pytest.mark.skip(reason="Вік не може бути менше 0")
def test_negative_age():
    """Skipping the test for incorrect age"""
    assert AgeVerifier.is_adult(-5) == False


age = 121

@pytest.mark.skipif(age > 120, reason="Неправильне значення віку")
def test_age_too_high():
    """Conditional skip for age > 120"""
    assert AgeVerifier.is_adult(age) == False
