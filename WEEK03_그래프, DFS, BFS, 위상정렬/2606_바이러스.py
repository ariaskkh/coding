from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n = int(input().strip())
m = int(input().strip())
cnt = 0
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
print(cnt-1)