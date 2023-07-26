"""
** Longest Substring Without Repeating Characters **
Given a string, find the length of the longest substring without repeating characters.
"""


def length_of_longest_substring(s):
    # The longest substring without repeating characters:
    max_length = 0
    # The current substring without repeating characters:
    current = ""

    for letter in s:
        # If the letter is not in the current substring, add it:
        if letter not in current:
            current += letter
        # If the letter is in the current substring, remove everything before it:
        else:
            index = (
                current.index(letter) + 1
            )  # find the next index after repeating character
            current = current[index:]  # update the current substring
            current += letter  # add the new letter

        # Update the longest substring:
        max_length = max(max_length, len(current))

    return max_length


def length_of_longest_substring_2(s):
    # The start of the sliding window:
    start = 0
    # The maximum length of a substring without repeating characters:
    max_length = 0
    # A dictionary to keep track of the characters in the current substring and their indices:
    char_map = {}

    for end in range(len(s)):
        # If the character is in the dictionary (and thus in the current substring),
        # move the start of the window past it:
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)

        # Add the character to the dictionary:
        char_map[s[end]] = end
        # Update the maximum length:
        max_length = max(max_length, end - start + 1)

    return max_length


# s = "abcabcbb"
s = "bbbbsjjaAjsssmnda"

print(length_of_longest_substring(s))

str = "berke"

print(str[2:])
print(str[:2])
