from graph import Graph

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self):
         """Adjacency matrix that holds graph data."""
        self.adj = {}
        self.count = 0

    def addVertex(self, vertex):
        if vertex in self.adj:
            return "Vert exists"
        if vertex != self.count:
            return "Do not vertex"
        self.adj[vertex] = []
        self.count += 1

    def addEdge(self, start, end, weight):
        if start not in self.adj:
            return "Start V not in graph"
        if end not in self.adj:
            return "End Vnot in graph"
        if start == end:
            return "Cannot have same start and end V"
        edge = Edge(start, end, weight)
        self.adj[start].append(edge)

    def doesEdgeExist(self, start, end):
        for vertex in self.adj:
            for edge in self.adj[vertex]:
                if edge.start == start and edge.end == end:
                    return (True, edge)
        return (False, None)

    def floydwarshall(self):
        """Floyd Warshall formula."""
        M = [[9999999 for x in range(len(self.adj))] for y in range(len(self.adj))]
        for x in range(len(M)):
            for y in range(len(M[0])):
                if x == y:
                    M[x][y] = 0
                exists, edge = self.doesEdgeExist(x, y)
                if exists:
                    M[x][y] = edge.weight
        for k in range(len(M)):
            for i in range(len(M)):
                for j in range(len(M)):
                    newDistance = M[i][k] + M[k][j]
                    if newDistance < M[i][j]:
                        M[i][j] = newDistance
        return M
