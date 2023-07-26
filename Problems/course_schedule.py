"""
** Course Schedule **
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

"""


def can_finish(numCourses, prerequisites):
    # Initialize the graph and the indegree array
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    # Build the graph and the indegree array
    for x, y in prerequisites:
        graph[y].append(x)
        indegree[x] += 1

    # Initialize a queue and add all nodes with indegree 0 into the queue
    queue = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    # Process nodes in the queue
    while queue:
        node = queue.pop(0)  # Remove the first node from the queue
        for x in graph[node]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)

    # Check if there's any node with indegree > 0
    for i in range(numCourses):
        if indegree[i] > 0:
            return False

    return True


# print(can_finish(2, [[1, 0]]))
# print(can_finish(2, [[1, 0], [0, 1]]))
print(can_finish(3, [[1, 0], [2, 1]]))
