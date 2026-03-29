""" Homework 8 task 9"""


class AgeVerifier:
    """Class for verifying the age of users"""

    @staticmethod
    def is_adult(age: int) -> bool:
        """Checks if the user is of legal age"""
        return age >= 18
