"""
** Two Sum **
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order.
"""


def two_sum(nums, target):
    num_map = {}  # Create an empty hash map

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:  # Check if the complement exists in the hash map
            return [num_map[complement], i]  # Return the indices
        num_map[num] = i  # Add the number and its index to the hash map

    return []  # Return an empty list if no solution is found


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))


# Two sum with two pointer method
def two_sum_two_pointer(nums, target):
    nums.sort()  # For two pointer method, we need to sort the array first
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return [left, right]

    return []


# nums = [2, 7, 11, 15]
nums = [3, 2, 4]
target = 6
# target = 9
print(two_sum_two_pointer(nums, target))
