"""
** Is Subsequence **
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""


def is_subsequence(s, t):
    si, ti = 0, 0  # initialize indices for s and t

    while si < len(s) and ti < len(t):
        if s[si] == t[ti]:
            si += 1  # move to next character in s
        ti += 1  # always move to next character in t

    # if we've gone through all characters in s, return True
    return si == len(s)


# Test
print(is_subsequence("abc", "ahbgdc"))  # True
print(is_subsequence("axc", "ahbgdc"))  # False
