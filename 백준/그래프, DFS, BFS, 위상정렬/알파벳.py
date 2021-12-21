# from collections import deque
# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline

# def bfs(a,b):
#     global mmax, cnt
#     #상0 우1 하2 좌3
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     # 순서 상관없이 있는지 여부만 확인하면 되므로 set으로 진행. queue로 할 경우 시간초과
#     queue = set()
#     queue.add((a,b,cnt,graph[a][b]))
#     while queue:
#         x, y, cnt1, before_visit = queue.pop()
#         # 네 방향 확인
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in before_visit: # 지금까지의 안 나온 알파벳이여야함
#                 queue.add((nx,ny, cnt1+1, before_visit+graph[nx][ny]))
#                 mmax = max(mmax, cnt1+1) 
        
#     print(mmax)

# R, C = map(int, input().split())
# graph = []
# for i in range(R):
#     graph.append(list(input().strip()))
# mmax = 1
# cnt = 1

# # (0,0 시작)
# bfs(0,0) 

# ##################################################################
# # set 안 쓰고 queue 쓰면 시간 초과
# from collections import deque
# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline

# def bfs(a,b):
#     global mmax, cnt
#     #상0 우1 하2 좌3
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]

#     queue = deque()
#     queue.append((a,b,cnt,graph[a][b]))
#     while queue:
#         x, y, cnt1, before_visit = queue.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in before_visit:
#                 queue.append((nx,ny, cnt1+1, before_visit+graph[nx][ny]))
#                 mmax = max(mmax, cnt1+1)
        
#     print(mmax)

# R, C = map(int, input().split())
# graph = []
# for i in range(R):
#     graph.append(list(input().strip()))
# mmax = 0
# cnt = 1

# bfs(0,0) 



######################################################
## 시간 초과 dfs

import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bt(x,y,lengg):
    global leng
    leng = max(leng, lengg)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # if arr[nx][ny] not in visited[x][y]:
            #     visited[nx][ny] = visited[x][y] + arr[nx][ny]
            #     bt(nx,ny, lengg+1)
            #     visited[nx][ny] = ''
            
            if arr[nx][ny] not in passed:
                passed.append(arr[nx][ny])
                bt(nx,ny, lengg+1)
                passed.remove(arr[nx][ny])

leng = 0
n, m = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]
visited = [[""] * (m+1) for _ in range(n)]
passed = [arr[0][0]]
# visited[0][0] += arr[0][0]


bt(0,0,1)
print(leng)


########################################################################################################################
## set으로 풀기.
##여기서 핵심은 방문했던 곳인 passed(visited)를 전역변수로 안하고 queue에 넣어 pop, add를 해 remove의 필요성을 없앤 것

import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(p,q):
    global mmax
    cnt = 1

    queue = set()
    queue.add((p,q,cnt, arr[0][0]))
    while queue:
        x, y, cnt, passed = queue.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] not in passed:
                    queue.add((nx,ny, cnt+1,passed + arr[nx][ny]))
                    mmax = max(mmax, cnt+1)
    print(mmax)

mmax = 1
n, m = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

bfs(0,0)