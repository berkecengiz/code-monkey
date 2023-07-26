"""
**Search Insert Position**
Given a sorted array of distinct integers and a target value;
If the target is found, return the index of the target.
If not, return the index where it would be if it were inserted in order.

Note: You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
"""


def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    # Perfom binary search
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Test the function
print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
