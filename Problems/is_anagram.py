"""
** Anagram Check **
Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact same letters
(so you can just rearrange the letters to get a different phrase or word).
For example:
"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
"""


# O(n) solution
def is_anagram(s, t):
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        else:
            char_count[char] -= 1
    return True


print(is_anagram("d go", "God"))


# O(n log n) solution
def is_anagram_with_sort(s, t):
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    return sorted(s) == sorted(t)


print(is_anagram("anagram", "nagaram"))
print(is_anagram_with_sort("anagram", "nagaram"))
