from collections import deque
import sys
input = sys.stdin.readline
########## bfs 리스트

# def bfs(start):
#     queue = deque([start])
#     visited[start] = True
#     while queue: # 재귀 대신 while 반복문 사용
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# n,m,v = map(int, input().split())
# visited = [False] * (n+1)
# graph = [] # 리스트로 구현
# for _ in range(n+1):
#     graph.append([])
# for i in range(m): # 무방향일때
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
# for i in range(1,n+1):
#     graph[i].sort()

# bfs(1)

########## dfs 행렬

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
visited = [0] *(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
bfs(v)