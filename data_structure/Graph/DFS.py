
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
#For connected graph
def dfs(g,N):
    s=list(g.keys())[0]
    visited=[False]*N
    dfs=[]

    def find_adjacent1(g,s,visited):
        visited[s]=True
        dfs.append(s)
        for ele in g[s]:
            if visited[ele]==False:
                find_adjacent1(g,ele,visited)
    find_adjacent1(g,s,visited)
    return dfs

# For disconnected graph

def find_adjacent(g,s,visited):
    visited[s]=True
    print(s,end=" ")
    for ele in g[s]:
        if visited[ele]==False:
            #print(ele)
            find_adjacent(g,ele,visited)


def dfs_disconnected(g,N):
    visited=[False]*N
    for i in range(0,N):
        if visited[i]==False:
            #print(i)
            find_adjacent(g,i,visited)

V=7
g=Graph(V)
g.add(0,1)
g.add(0,2)
g.add(1,3)
g.add(2,3)
g.add(4,5)
g.add(5,6)
g.add(4,6)
print_graph(g.graph)

dfs_disconnected(g.graph,7)


V=9
g=Graph(V)
g.add(0,1)
g.add(1,2)
g.add(0,2)
g.add(3,4)
g.add(5,6)
g.add(5,8)
g.add(7,8)
print_graph(g.graph)

dfs_disconnected(g.graph,9)




















"""V=7
g=Graph(V)
g.add(0,1)
g.add(0,2)
g.add(2,3)
g.add(1,3)
g.add(1,4)
g.add(4,5)
print_graph(g.graph)
print(dfs(g.graph,0,7))"""

"""V=15
g=Graph(V)
g.add(0,3)
g.add(0,4)
g.add(0,6)
g.add(0,8)
g.add(0,13)
g.add(1,4)
g.add(1,13)
g.add(3,5)
g.add(3,11)
g.add(3,13)
g.add(4,10)
g.add(5,7)
g.add(5,10)
g.add(5,12)
g.add(5,13)
g.add(9,12)
g.add(10,11)
g.add(10,14)
print_graph(g.graph)
print(dfs(g.graph,15))"""
#0 3 5 7 10 4 1 13 11 14 12 2 9 6 8
#0 3 5 7 10 4 1 13 11 6 8 14 12 2 9
