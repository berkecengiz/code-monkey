"""
** Find the difference between two arrays **

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""


def find_difference(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    return [list(nums1 - nums2), list(nums2 - nums1)]


# Test

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 6, 7]
print(find_difference(nums1, nums2))


def find_difference_hash_map(nums1, nums2):
    nums1_map = {}
    nums2_map = {}

    # Create hash maps for nums1 and nums2
    for num in nums1:
        nums1_map[num] = True

    for num in nums2:
        nums2_map[num] = True

    nums1_diff = []
    nums2_diff = []

    # Check for differences
    for num in nums1:
        if num not in nums2_map:
            nums1_diff.append(num)

    for num in nums2:
        if num not in nums1_map:
            nums2_diff.append(num)

    return [nums1_diff, nums2_diff]


# Test

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 6, 7]

print(find_difference_hash_map(nums1, nums2))
