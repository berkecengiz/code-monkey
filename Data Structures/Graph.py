"""Implementation of Graph data structure.

A graph is a data structure that consists of the following two components:
    1. A finite set of vertices also called as nodes.
    2. A finite set of ordered pair of the form (u, v) called as edge.
      The pair is ordered because (u, v) is not same as (v, u) in case of a directed graph(di-graph)
      The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v.
      The edges may contain weight/value/cost.
"""


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

        if node2 in self.graph:
            self.graph[node2].append(node1)
        else:
            self.graph[node2] = [node1]

    def remove_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].remove(node2)
        if node2 in self.graph:
            self.graph[node2].remove(node1)

    def display_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)  # pop the first element
            if node not in visited:
                visited.add(node)
                print(node)
                queue.extend(self.graph[node])
        return visited

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()  # pop the last element
            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(self.graph[node])
        return visited


g = Graph()
g.add_node("A")
g.add_node("B")
g.add_edge("A", "B")
print(g.graph)
g.display_graph()  # Outputs: {'A': ['B'], 'B': []}

g.remove_node("A")
print(g.graph)
g.display_graph()  # Outputs: {'B': []}

g.add_node("C")
g.add_node("D")
