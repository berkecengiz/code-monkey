"""
** Minimum Size Subarray Sum **
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""


def min_sub_array_length(target, nums):
    min_length = float("inf")
    left = 0
    current_sum = 0
    # Iterate through the array
    for right in range(len(nums)):
        # Add the current number to the sum
        current_sum += nums[right]
        # If the sum is greater than or equal to the target, increment left
        while current_sum >= target:
            # Update the min length
            min_length = min(min_length, right - left + 1)
            # Subtract the left number from the sum
            current_sum -= nums[left]
            # Increment left
            left += 1
    # Return the min length
    return min_length if min_length != float("inf") else 0


# Test the function
print(min_sub_array_length(7, [2, 3, 1, 2, 4, 3]))
