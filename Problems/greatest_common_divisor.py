"""
** Greatest Common Divisor **

For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example:


Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

"""


def gcd_of_strings(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    left = str1[: len(str2)]
    right = str1[len(str2) :]

    if left == str2 and right == "":
        return str2

    if left == str2:
        return gcd_of_strings(right, str2)

    return ""


# Test

print(gcd_of_strings("ABCABC", "ABC"))
print(gcd_of_strings("ABABAB", "ABAB"))
print(gcd_of_strings("ABCDEF", "ABC"))
