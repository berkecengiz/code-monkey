"""
** Problem: Unique Number of Occurrences

Given an array of integers arr, write a function that returns true if
and only if the number of occurrences of each value in the array is unique.

"""


def unique_occurences(arr):
    num_map = {}
    for num in arr:
        # If the number exists in the hash map, increment its value by 1
        if num in num_map:
            num_map[num] += 1
        # Else, add the number to the hash map and set its value to 1
        else:
            num_map[num] = 1

    unique_values = set(num_map.values())

    return len(num_map) == len(unique_values)


print(unique_occurences([1, 2, 2, 1, 1, 3]))
print(unique_occurences([1, 2]))
print(unique_occurences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
