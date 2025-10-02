from queue import Queue
from queue import LifoQueue
import numpy as np
n=8
adjMat = np.zeros((n+1,n+1), dtype = int)
print(adjMat)
def addEdgeToMatrix(source,destination):
    adjMat[source][destination] = 1
    adjMat[destination][source] = 1

def bfs(adjMat, source):
    visited = np.zeros(n+1, dtype = int)
    q = Queue()
    visited[source] = 1
    q.put(source) #enqueue
    while q.empty() != True:
        u = q.get() #dequeue
        print(u, end = " ")
        for v in range(len(adjMat[u])): #searching connection of the dequeued node
            if adjMat[u][v] == 1 and visited[v] == 0:
                visited[v] = 1
                q.put(v)

def dfs(adjMat, source):
    visited = np.zeros(n+1, dtype = int)
    stack = LifoQueue()
    visited[source] = 1
    stack.put(source) #enqueue
    while stack.empty() != True:
        u = stack.get() #dequeue
        print(u, end = " ")
        for v in range(len(adjMat[u])): #searching connection of the dequeued node
            if adjMat[u][v] == 1 and visited[v] == 0:
                visited[v] = 1
                stack.put(v)   

addEdgeToMatrix(1,2)
addEdgeToMatrix(1,4)
addEdgeToMatrix(2,3)
addEdgeToMatrix(2,5)
addEdgeToMatrix(3,4)
addEdgeToMatrix(3,6)
addEdgeToMatrix(3,8)
addEdgeToMatrix(6,7)
print()
print(adjMat)
print()
bfs(adjMat,3)
print()
dfs(adjMat,3)