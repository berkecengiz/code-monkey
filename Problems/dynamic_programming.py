"""Leetcode Dynamic Programming Questions"""


def longest_common_subsequence(text1, text2):
    """
    ** Longest Common Subsequence **
    Given two strings, find the longest common subsequence (LCS).

    Args:
        text1 (str): First string
        text2 (str): Second string

    Returns:
        int: Length of the longest common subsequence
    """

    # Make sure text1 is longer than text2
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    # Initialize the previous row
    prev = [0] * (len(text2) + 1)

    # Iterate through the rows
    for i in range(1, len(text1) + 1):
        curr = [0]
        # Iterate through the columns
        for j in range(1, len(text2) + 1):
            # If the characters match, add 1 to the previous diagonal
            if text1[i - 1] == text2[j - 1]:
                curr.append(prev[j - 1] + 1)
            # Otherwise, take the max of the previous row and column
            else:
                curr.append(max(prev[j], curr[-1]))
        # Update the previous row
        prev, curr = curr, prev

    # Return the last element of the previous row
    return prev[-1]


# Test the function
print("Longest Common Subsequence")
print(longest_common_subsequence("abcde", "ace"))  # 3 ("ace")


def longest_increasing_subsequence(nums):
    """
    ** Longest Increasing Subsequence **
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    Args:
        nums (list): List of integers

    Returns:
        int: Length of the longest strictly increasing subsequence
    """

    # Initialize the longest subsequence array
    longest = [1] * len(nums)

    # Iterate through the array
    for i in range(1, len(nums)):
        # Iterate through the previous elements
        for j in range(i):
            # If the current element is greater than the previous element,
            # update the longest subsequence array
            if nums[i] > nums[j]:
                longest[i] = max(longest[i], longest[j] + 1)

    # Return the max of the longest subsequence array
    return max(longest)


# Test the function
print("Longest Increasing Subsequence")
print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))  # 4


def tallest_stack(cuboids):
    """
        ** Tallest Stack **

    Given n cuboids where the dimensions of the ith cuboid is
    cuboids[i] = [widthi, lengthi, heighti] (0-indexed).

    Choose a subset of cuboids and place them on each other.

    You can place cuboid i on cuboid j
        if widthi <= widthj and lengthi <= lengthj and heighti <= heightj.
    You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

    Return the maximum height of the stacked cuboids.


    Args:
        boxes (list): List of boxes

    Returns:
        int: Height of the tallest stack of boxes
    """

    for box in cuboids:
        box.sort()  # Sort dimensions of each box
    cuboids.append([0, 0, 0])  # Append a dummy box of zero height
    cuboids.sort()  # Sort the cuboids

    dp = [0] * (len(cuboids))  # Initialize the dp table

    for i in range(len(cuboids)):
        print(dp)
        # The height is the maximum height if the box itself is considered
        dp[i] = cuboids[i][2]
        for j in range(i):
            # Check if box j can be put on box i
            if (
                # If the dimensions of box j are less than or equal to box i
                cuboids[i][0] >= cuboids[j][0]
                and cuboids[i][1] >= cuboids[j][1]
                and cuboids[i][2] >= cuboids[j][2]
            ):
                # Update the maximum height
                dp[i] = max(dp[i], dp[j] + cuboids[i][2])
    return max(dp)  # Return the maximum height among all options


# Test
print("Tallest Stack")
cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
print(tallest_stack(cuboids))  # 190


def longest_nondecreasing_subarray(nums1, nums2):
    """
    ** Longest Nondecreasing Subarray **
    Given two integer arrays A and B,
    return the maximum length of an subarray that appears in both arrays.

    Args:
        nums1 (list): First array
        nums2 (list): Second array

    Returns:
        int: Length of the longest nondecreasing subarray
    """

    n = len(nums1)
    dp = [[1] * n, [1] * n]

    for i in range(1, n):
        if nums1[i] >= nums1[i - 1]:
            dp[0][i] = max(dp[0][i], 1 + dp[0][i - 1])
        if nums1[i] >= nums2[i - 1]:
            dp[0][i] = max(dp[0][i], 1 + dp[1][i - 1])
        if nums2[i] >= nums1[i - 1]:
            dp[1][i] = max(dp[1][i], 1 + dp[0][i - 1])
        if nums2[i] >= nums2[i - 1]:
            dp[1][i] = max(dp[1][i], 1 + dp[1][i - 1])

    print(dp)
    return max(max(dp[0]), max(dp[1]))


# Test
print("Longest Nondecreasing Subarray")

nums1 = [1, 3, 2, 1]
nums2 = [2, 2, 3, 4]
print(longest_nondecreasing_subarray(nums1, nums2))  # 3
