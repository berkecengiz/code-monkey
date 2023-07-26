"""
** Problem: Move Zeroes **

Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.
"""


def move_zeroes(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] != 0:  # if the current element is not 0, move it to the front
            nums[count] = nums[i]
            count += 1

    while count < len(nums):
        nums[count] = 0  # fill the rest of the array with 0
        count += 1

    return nums


print(move_zeroes([0, 1, 0, 3, 12]))
