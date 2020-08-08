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
V=8
g=Graph(V)
g.add(1,2)
g.add(1,5)
g.add(1,4)
g.add(2,7)
g.add(2,6)
g.add(2,3)
print_graph(g.graph)


"""V=4
g=Graph(V)
g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(1,3)
print_graph(g.graph)"""





#print(bfs(g.graph))

def bfs(g,N):

        # Mark all the vertices as not visited
    visited = [False] * N
    s=list(g.keys())[0]

    # Create a queue for BFS
    # Mark the source node as
    # visited and enqueue it
    queue=[]
    queue.append(s)
    visited[s] = True
    bfs=[]
    while queue:
        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        bfs.append(s)
        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in g[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return bfs
print(bfs(g.graph,8))

# The code below is for unconnected graph.


def bfs0(g,visited,i):

    # Create a queue for BFS
    # Mark the source node as
    # visited and enqueue it
    queue=[]
    queue.append(i)
    visited[i] = True
    while queue:
        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        #print(s,end=" ")
        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in g[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


def bfs_disconnected(g,N):
    # Mark all the vertices as not visited
    visited = [False] * N
    count=0
    for i in range(N):
        if visited[i]==False:
            count+=1
            bfs0(g,visited,i)
    return count

V=8
g=Graph(V)
g.add(0,1)
g.add(1,2)
g.add(0,2)
g.add(3,4)
g.add(5,6)
g.add(5,7)
g.add(7,8)
print_graph(g.graph)

print(bfs_disconnected(g.graph,9))
