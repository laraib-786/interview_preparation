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

def shortest_path(g,N):
    visited = [False] * N
    s=list(g.keys())[0]
    queue=[]
    queue.append(s)
    visited[s] = True
    dist=[10**6]*N
    dist[s]=0

    while queue:
        s = queue.pop(0)

        for i in g[s]:
            if visited[i] == False:
                queue.append(i)
                dist[i]=dist[s]+1
                visited[i] = True
    return dist

V=6
g=Graph(V)
g.add(0,1)
g.add(0,4)
g.add(0,2)
g.add(2,3)
g.add(2,4)
g.add(4,5)
g.add(3,5)
print_graph(g.graph)

print(shortest_path(g.graph,6))

V=4
g=Graph(V)
g.add(0,1)
g.add(1,3)
g.add(0,2)
g.add(1,2)
print_graph(g.graph)

print(shortest_path(g.graph,4))
