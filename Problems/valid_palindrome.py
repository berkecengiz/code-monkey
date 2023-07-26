"""
** Valid Palindrome **
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
"""


def is_palindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters
    s = "".join(char for char in s if char.isalnum())

    # Convert string to lowercase
    s = s.lower()

    # Check if string is a palindrome
    return s == s[::-1]
