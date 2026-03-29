""" Homework 8 task 6 Tests"""


from unittest import mock
import pytest
from hw_8_6 import BankAccount


@pytest.fixture
def empty_account():
    """Empty score before each test"""
    return BankAccount()


@pytest.fixture
def preloaded_account():
    """Account with opening balance"""
    return BankAccount(initial_balance=100.0)


@pytest.mark.parametrize(
    "initial, deposit_amount, expected",
    [
        (0, 50, 50),
        (100, 50, 150),
        (20, 0, 20),
        (0, 0, 0),
    ]
)
def test_deposit_param(empty_account, initial, deposit_amount, expected):
    """Test deposit with params"""
    account = BankAccount(initial)
    account.deposit(deposit_amount)
    assert account.get_balance() == expected


@pytest.mark.parametrize(
    "initial, withdraw_amount, expected",
    [
        (100, 50, 50),
        (100, 100, 0),
        (50, 25, 25),
    ]
)
def test_withdraw_param(initial, withdraw_amount, expected):
    """Test withdraw with params"""
    account = BankAccount(initial)
    account.withdraw(withdraw_amount)
    assert account.get_balance() == expected


def test_withdraw_insufficient(preloaded_account):
    """Test withdraw with insufficient balance"""
    with pytest.raises(ValueError, match="Insufficient funds"):
        preloaded_account.withdraw(200)


def test_skip_if_empty(empty_account):
    """Test skip if empty account"""
    if empty_account.get_balance() == 0:
        pytest.skip("Рахунок порожній, тест пропускається")
    empty_account.withdraw(10)


def test_balance_check_with_mock(preloaded_account):
    """Test balance check with mock"""
    with mock.patch.object(preloaded_account, 'get_balance', return_value=500.0):
        assert preloaded_account.get_balance() == 500.0
        preloaded_account.get_balance.assert_called_once()
