from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
def print_graph(adj):
    for key,values in adj.items():
        print(key,end="")
        for value in values:
            print("->{}".format(value),end="")
        print("")



"""
V=8
g=Graph(V)
g.add(1,2)
g.add(1,5)
g.add(1,4)
g.add(2,7)
g.add(2,6)
g.add(2,3)
print_graph(g.graph)"""

V=4
g=Graph(V)
g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(1,3)
print_graph(g.graph)
