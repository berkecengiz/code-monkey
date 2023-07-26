"""
** Contains Duplicate **
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


def contains_duplicate(nums):
    num_map = {}

    for num in nums:
        if num in num_map:
            return True
        num_map[num] = True

    return False


print(contains_duplicate([1, 2, 3, 7, 4, 5, 6, 7, 8, 9, 10]))


def contains_duplicate_two(nums):
    return len(nums) != len(set(nums))
