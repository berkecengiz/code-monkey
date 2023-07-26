"""
** Problem: Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.


Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6

Explanation:
A=[1,1,1,0,0,0,1,1,1,1,0]
R=[1,1,1,0,0,1,1,1,1,1,1]
"""


def longest_ones(nums, k):
    left = 0
    for right in range(len(nums)):
        # If we encounter a zero, decrement k.
        if nums[right] == 0:
            k -= 1
        # If k becomes negative, slide the window to the right.
        if k < 0:
            # If the left element going out was zero, we increment k.
            if nums[left] == 0:
                k += 1
            left += 1
    # When the loop ends, right is at the end of the array,
    # so the length of the window is right - left + 1.
    return right - left + 1


# Test

print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 2))  # 9
print(longest_ones([0, 0, 0, 1, 0, 0, 0, 1], 2))  # 3
