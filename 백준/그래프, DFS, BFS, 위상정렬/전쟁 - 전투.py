# ## DFS 방식

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# visited = [[0]*(N) for _ in range(M)]
# arr =[]
# cntw=0
# cntb=0
# ans1 = []
# ans2 = []
# for _ in range(M):
#     arr.append(list(input().strip()))

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def dfsw(x,y):
#     global cntw, cntb
#     if arr[x][y] == 'W' and visited[x][y] == 0:
#         visited[x][y] = 1
#         cntw +=1
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
#                 if arr[nx][ny] == 'W':
#                     dfsw(nx,ny)
# def dfsb(x,y):
#     global cntw, cntb
#     if arr[x][y] == 'B' and visited[x][y] == 0:
#         visited[x][y] = 1
#         cntb +=1
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
#                 if arr[nx][ny] == 'B':
#                     dfsb(nx,ny)

# for p in range(M):
#     for q in range(N):
#         dfsw(p,q)
#         if cntw != 0:
#             ans1.append(cntw*cntw)
#             cntw = 0
#         dfsb(p,q)
#         if cntb != 0:
#             ans2.append(cntb*cntb)
#             cntb = 0

# print(sum(ans1), end=" ")
# print(sum(ans2))

### BFS 방식

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(input().strip()) for _ in range(M)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(s,d, strr):
    global cnt
    queue = deque()
    queue.append((s,d))
    graph[s][d] = 0
    cnt += 1
    while(queue):
        # print(queue)
        x,y = queue.popleft()
        # print("x,y:",x,y)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx >=0 and ny >= 0 and nx < M and ny < N:
                if graph[nx][ny] != 0 and graph[nx][ny ]== strr:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
                    cnt +=1
cnt=0
W = 0
B = 0
for p in range(M):
    for q in range(N):
        if graph[p][q] != 0:
            if graph[p][q] == "W":
                bfs(p, q, graph[p][q])
                W += cnt*cnt
            else:
                bfs(p, q, graph[p][q])
                B += cnt*cnt
            cnt =0
print(W, end=" ")
print(B)