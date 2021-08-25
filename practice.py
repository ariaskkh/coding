from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph =[[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topo():
    queue = deque()
    result = []
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        x = queue.popleft()
        result.append(x)
        for j in graph[x]:
            indegree[j] -= 1
            if indegree[j] ==0:
                queue.append(j)
    for k in result:
        print(k, end= ' ')

topo()