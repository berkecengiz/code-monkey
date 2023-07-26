"""
**Pow(x, n)**
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


def my_pow(x, n):
    # Compute x^n recursively, given n >= 0.
    if n == 0:
        # Base case: x^0 = 1.
        return 1
    elif n < 0:
        # x^(-n) = 1/(x^n).
        return 1 / my_pow(x, -n)
    elif n % 2:
        # x^n = x*x^(n-1).
        return x * my_pow(x, n - 1)
    else:
        # x^n = (x*x)^(n/2).
        return my_pow(x * x, n // 2)


def my_pow_2(x, n):
    # Compute x^n iteratively, given n >= 0.
    result = 1
    while n > 0:
        if n % 2:
            # n is odd.
            result *= x
        x *= x
        n //= 2
    return result


# Test the function
print(my_pow(2, 10))
print(my_pow_2(3, 3))
