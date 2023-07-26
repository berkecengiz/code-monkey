"""
** Three Sum **
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # skip same result
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:  # if sum < 0, increment left
                left += 1
            elif total > 0:  # if sum > 0, decrement right
                right -= 1
            else:  # sum = 0
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # skip same result
                    left += 1
                while (
                    left < right and nums[right] == nums[right - 1]
                ):  # skip same result
                    right -= 1
                left += 1
                right -= 1
    return result


# Test the function
print(three_sum([2, 7, 11, 15], 9))
