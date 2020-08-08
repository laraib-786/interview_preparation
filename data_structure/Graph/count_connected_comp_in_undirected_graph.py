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
def find_adjacent(g,s,visited):
    visited[s]=True
    #print(s,end=" ")
    for ele in g[s]:
        if visited[ele]==False:
            find_adjacent(g,ele,visited)


def dfs_disconnected(g,N):
    visited=[False]*N
    count=0
    for i in range(0,N):
        if visited[i]==False:
            find_adjacent(g,i,visited)
            count+=1
    return count

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

print(dfs_disconnected(g.graph,7))


"""V=9
g=Graph(V)
g.add(0,1)
g.add(1,2)
g.add(0,2)
g.add(3,4)
g.add(5,6)
g.add(5,8)
g.add(7,8)
print_graph(g.graph)
print(dfs_disconnected(g.graph,9))"""




def bfs0(g,visited,i,parent):
    queue=[]
    queue.append(i)
    visited[i] = True
    while queue:
        s = queue.pop(0)
        for i in g[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                if bfs0(g,visited,i,s)==True:
                    return True
    return False


def bfs_disconnected(g,N):
    visited = [False] * N
    for i in range(N):
        if visited[i]==False:
            if bfs0(g,visited,i,-1)==True:
                return True
    return False
