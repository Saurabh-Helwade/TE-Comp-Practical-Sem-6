class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self , u, v, w):
        self.graph.append( [u, v, w] )
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent , parent[i])
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot]  = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def kruskal_algo(self):
        result = []
        i , e = 0 , 0
        self.graph = sorted(self.graph, key=lambda item: item[2] )
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y :
                e = e + 1
                result.append([u,v,w])
                self.apply_union(parent, rank, x , y)
        minimum_cost = 0
        print("kruskal algorithm :- \n")
        print("Edge  | Weight ")
        for u , v , weight in result:
            minimum_cost += weight
            print("%d - %d :- %d" % ( u , v, weight))
        print("\nWeight Of Minimum Spanning Tree :-", minimum_cost)
            
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 5)
g.add_edge(0, 4, 3)
g.add_edge(0, 2, 8)
g.add_edge(4, 0, 3)
g.add_edge(1, 0, 4)
g.add_edge(1, 3, 2)
g.add_edge(3, 1, 2)
g.add_edge(3, 0, 8)
g.add_edge(3, 4, 1)
g.add_edge(4, 3, 8)
g.add_edge(2, 4, 4)
g.add_edge(2, 0, 5)
g.add_edge(4, 2, 4)
g.kruskal_algo()
