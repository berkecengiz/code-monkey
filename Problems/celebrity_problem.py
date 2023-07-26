"""
**Celebrity Problem**
In a party of N people, only one person is known to everyone.
Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party.
We can only ask questions like “does A know B? “.
Find the stranger (celebrity) in the minimum number of questions.
"""


def find_celebrity(people):
    # The two people we're comparing:
    a = 0
    b = 1
    # The number of people:
    N = len(people)

    # Step 1: Find the celebrity candidate:
    while b < N:
        # If a knows b, then a can't be the celebrity:
        if people[a][b]:
            a = b
        b += 1

    # Step 2: Check that the candidate is actually a celebrity:
    for i in range(N):
        if i != a and (people[a][i] or not people[i][a]):
            return -1

    return a


# M = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
M = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Person 0
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Person 1
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Person 2
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Person 3
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Person 4
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # Person 5
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # Person 6
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # Person 7
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # Person 8
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # Person 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # Person 10
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # Person 11
]

M_2 = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Person 0
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Person 1
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # Person 2
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # Person 3
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # Person 4
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],  # Person 5
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],  # Person 6
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # Person 7
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # Person 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Person 9 (celebrity)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # Person 10
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],  # Person 11
]


print(find_celebrity(M))
print(find_celebrity(M_2))
