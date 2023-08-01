"""
** Merge Strings **

You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the string.

Return the merged string.
"""


def merge_alternately(word1, word2):
    merged = ""

    for i in range(min(len(word1), len(word2))):
        merged += word1[i]
        merged += word2[i]

    if len(word1) > len(word2):
        merged += word1[i + 1:]  # fmt: skip
    if len(word2) > len(word1):
        merged += word2[i + 1:]  # fmt: skip

    return merged


# Test
print(merge_alternately("abc", "def"))  # adbecf
