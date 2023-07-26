"""
** Palindrome Number **
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.
"""


def is_palindrome(self, x: int) -> bool:
    str_x = str(x)

    first = 0
    last = len(str_x) - 1

    while first < last:
        if str_x[first] != str_x[last]:
            return False
        first = first + 1
        last = last - 1

    return True
