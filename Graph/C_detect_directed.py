
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
def print_graph(adj):
    for key,values in adj.items():
        print(key,end="")
        for value in values:
            print("->{}".format(value),end="")
        print("")
# Code for cycle detection of nonconnected graph.
def dfs_r(g,s,visited,rec_s):
    visited[s]=True
    rec_s[s]=True
    for adj in g[s]:
        if visited[adj]==False:
            if dfs_r(g,adj,visited,rec_s)==True:
                return True
        elif rec_s[adj]==True:
                return True
    rec_s[s]=False # for recursion calling stack if there is not a adj of any node it revert back and false every node one by one
    return False
def dfs(g,N):
    visited=[False]*N
    rec_s=[False]*N
    for i in range(0,N):
        if visited[i]==False:
            if dfs_r(g,i,visited,rec_s)==True:
                return True
    return False


#0---->1---->2<-----3
V=4
g=Graph(V)
g.add(0,1)
g.add(1,2)
g.add(2,3)
print_graph(g.graph)

print(dfs(g.graph,4))




#0---->1---->2
#     ^      /
#      \    /
#        3 <
V=4
g=Graph(V)
g.add(0,1)
g.add(1,2)
g.add(2,3)
g.add(3,1)
print_graph(g.graph)

print(dfs(g.graph,4))
#0---->1<----2
#     ^      /
#      \    /
#        3 <

V=4
g=Graph(V)
g.add(0,1)
g.add(2,1)#change
g.add(2,3)
g.add(3,1)
print_graph(g.graph)

print(dfs(g.graph,4))
