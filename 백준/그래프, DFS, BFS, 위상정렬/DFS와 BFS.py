# 연결 리스트를 이용 

from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int,input().split())# 정점, 간선, 출발점

graph = [[] for _ in range(N+1)]
visited = [False] *(N+1)

for i in range(1, M+1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, v, visited): # 그래프, 시작점, 방문지점
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited): # 그래프, 시작점, 방문지점
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, V, visited)
print()
visited = [False] *(N+1)
bfs(graph, V, visited)


##########################################################################################################
# 연결 행렬을 이용. 행렬 전체를 처음에 만듦

from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if  graph[v][i] ==1 and visited[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
visited = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
visited = [0] * (n+1)
bfs(v)