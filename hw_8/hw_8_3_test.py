""" Homework 8 task 3 Test"""


import pytest
from hw_8_3 import UserManager


@pytest.fixture
def u_manager():
    """Fixture for user manager"""
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def test_add_user(u_manager):
    """Test adding users"""
    u_manager.add_user("Charlie", 20)
    users = u_manager.get_all_users()
    assert {"name": "Charlie", "age": 20} in users
    assert len(users) == 3


def test_remove_user(u_manager):
    """Test removing users"""
    u_manager.remove_user("Alice")
    users = u_manager.get_all_users()
    assert {"name": "Alice", "age": 30} not in users
    assert len(users) == 1


def test_get_all_users(u_manager):
    """Test getting all users"""
    users = u_manager.get_all_users()
    assert len(users) == 2
    assert {"name": "Alice", "age": 30} in users
    assert {"name": "Bob", "age": 25} in users


def test_skip_if_few_users(u_manager):
    """Test skipping users"""
    if len(u_manager.get_all_users()) < 3:
        pytest.skip("Мало користувачів, тест пропускається")
    # цей код ніколи не виконається у нашому випадку
    u_manager.add_user("Charlie", 20)
    users = u_manager.get_all_users()
    assert {"name": "Charlie", "age": 20} in users
