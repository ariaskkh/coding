# from collections import deque
# import sys
# input = sys.stdin.readline

# # bfs로 풀이
# #상 0 우 1 하 2 좌 3
# def bfs(a,b):
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     queue = deque()
#     queue.append([a,b])
#     visited[a][b] = 1
#     dist[a][b] = 1
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 1 and visited[nx][ny] == 0:
#                     queue.append([nx,ny])
#                     visited[nx][ny] = 1
#                     dist[nx][ny] = dist[x][y] +1

# n, m = map(int, input().strip().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input().strip())))
# visited = [[0] * m for _ in range(n)]
# dist = [[0] * m for _ in range(n)]

# bfs(0,0)
# print(dist[n-1][m-1])

############################################################
# 다시 풀기 108ms 최소기록 !

import sys
input =sys.stdin.readline
from collections import deque

X, Y = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(X)]
visited = [[0] * (Y+1) for _ in range(X+1)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(p,q):
    queue = deque()
    queue.append([p,q])
    visited[p][q] = 1
    while queue:
        print(queue)
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < X and  0<= ny < Y:
                if not visited[nx][ny] and graph[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1


bfs(0,0)
print(visited[X-1][Y-1])


