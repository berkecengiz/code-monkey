"""
** Maximum Average Subarray **
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value.
Any answer with a calculation error less than 10-5 will be accepted.
"""


def find_max_avg(nums, k):
    # Calculate the sum of the first 'k' elements
    current_sum = sum(nums[0:k])
    # This is the maximum sum we've seen so far
    max_sum = current_sum

    # Iterate over the rest of the array
    for i in range(k, len(nums)):
        # Slide the window to the right by subtracting the element on the left
        # (nums[i - k]) and adding the element on the right (nums[i])
        current_sum = current_sum - nums[i - k] + nums[i]
        # If the current sum is greater than the maximum sum, update the maximum sum
        max_sum = max(max_sum, current_sum)

    # Return the average of the maximum sum
    return max_sum / k


print(find_max_avg([1, 12, -5, -6, 50, 3], 4))
