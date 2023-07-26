"""
**Climbing Stairs**

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

"""


def climb_stairs(n):
    if n <= 2:
        return n

    one_step_before = 2
    two_steps_before = 1

    for _ in range(3, n + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current

    return one_step_before


n = 5
print(climb_stairs(n))
