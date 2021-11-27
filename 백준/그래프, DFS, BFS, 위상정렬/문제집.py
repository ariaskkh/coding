from collections import deque
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
# print(graph)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topo_sort():
    p_queue = []
    result = []
    for i in range(1,N+1):
        if indegree[i] == 0:
            heapq.heappush(p_queue, i)
    while p_queue:
        x = heapq.heappop(p_queue)
        # x.sort()
        result.append(x)
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] ==0 :
                heapq.heappush(p_queue, i)
    for j in result:
        print(j, end=' ')

topo_sort()