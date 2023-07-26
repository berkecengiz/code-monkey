"""
** Reverse Integer **
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside 32-bit integer range [-231, 231 - 1] return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


def reverse(x):
    # Check if the number is negative
    negative = False
    if x < 0:
        negative = True
        x = -x
    # Reverse the number
    reversed = 0
    while x > 0:
        # Multiply the reversed number by 10 and add the last digit of x
        reversed = reversed * 10 + x % 10
        # Remove the last digit of x
        x //= 10
    # Check if the number is out of range
    if reversed > 2**31 - 1:
        return 0
    # Return the reversed number
    return -reversed if negative else reversed


# Test the function
print(reverse(123))
print(reverse(-123))
