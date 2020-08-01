""" The logic behind this is that if in a chain the last element has adjacent
 other than the parent then there is cycle"""
#eg: 0--1   and   2--3
#                 |  |
#                 5--4

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
# Code for cycle detection of nonconnected graph.
def dfs_r(g,s,visited,parent):
    visited[s]=True
    for adj in g[s]:
        if visited[adj]==False:
            if dfs_r(g,adj,visited,s)==True:
                return True
        elif (adj != parent):
                return True
    return False
def dfs(g,N):
    visited=[False]*N
    for i in range(0,N):
        if visited[i]==False:
            if dfs_r(g,i,visited,-1)==True:
                return True
    return False
V=6
g=Graph(V)
g.add(0,1)
g.add(2,3)
g.add(3,4)
g.add(4,5)
g.add(5,2)
print_graph(g.graph)

print(dfs(g.graph,6))


def bfs0(g,visited,i,N):
    queue=[]
    queue.append(i)
    parent=[-1]*N # parent array
    visited[i] = True
    while queue:
        s = queue.pop(0)
        for i in g[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                parent[i]=s  # first queue has [0] which pops up and 1 is adj it get in to queue [1] ,this line is meant for next loop 1 pops up zero is adj of
            elif parent[i]==s:
                return True
    return False


def bfs_disconnected(g,N):
    visited = [False] * N
    for i in range(N):
        if visited[i]==False:
            if bfs0(g,visited,i,N)==True:
                return True
    return False
V=2
g=Graph(V)
g.add(0,1)
"""g.add(2,3)
g.add(3,4)
g.add(4,5)
g.add(5,2)"""
print_graph(g.graph)

print(bfs_disconnected(g.graph,2))
