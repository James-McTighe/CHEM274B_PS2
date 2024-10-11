class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

class DisjointSet:
    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

class Solution:
    def kruskal_mst(self, graph):
        # TODO: Implement
        pass

    def is_cyclic_util(self, graph, v, visited, parent):
        # TODO: Implement
        pass

    def is_cyclic(self, graph):
        # TODO: Implement
        pass

    def detect_deadlock(self, graph):
        # TODO: Implement
        pass