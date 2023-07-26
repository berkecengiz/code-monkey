"""
Given a list of n strings. Each string has length k.
Return true if there're 2 strings that only differ by 1 character, otherwise false.
You can assume that all strings contain only lowercase English letters [a-z].

Example 1:
Input: ["abc", "xyz", "abd"]
Output: true
Explanation: "abc" and "abd" only differ by 1 character.

Example 2:
Input: ["abc", "def", "xyz"]
Output: false

Example 3:
Input: ["abcd", "bbbb", "abxd", "cccc"]
Output: true

"""


def check_one_difference(array):
    # Create a hash table
    hash_table = set()

    for string in array:
        for i in range(len(string)):
            # Replace one character with a wildcard
            wildcard_string = string[:i] + "*" + string[i + 1 :]

            # If we have seen this string before, return True
            if wildcard_string in hash_table:
                return True

            # Otherwise, add it to our hash table
            hash_table.add(wildcard_string)

    # If no match was found, return False
    return False


# Test
print(check_one_difference(["abc", "xyz", "abd"]))  # True
print(check_one_difference(["abc", "def", "xyz"]))  # False
print(check_one_difference(["abcd", "bbbb", "abxd", "cccc"]))  # True
