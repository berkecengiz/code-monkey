"""
** String Compression **

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead,
be stored in the input character array chars.

Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space
"""


def compress(chars):
    i, count, length = 0, 1, len(chars)
    for j in range(1, length + 1):
        if j < length and chars[j] == chars[j - 1]:
            count += 1
        else:
            if count > 1:
                for digit in str(count):
                    chars[i + 1] = digit
                    i += 1
            if j < length:
                chars[i + 1] = chars[j]
                i += 1
            count = 1
    return i + 1


# Test cases
print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))
