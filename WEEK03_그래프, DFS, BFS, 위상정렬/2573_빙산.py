
#################################################################
# 다른 사람 정답, python으로 통과 가능

import sys
from collections import deque


def bfs():
    attached = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque([ice[0]])
    visited[ice[0][0]][ice[0][1]] = True
    while q:
        x, y = q.popleft()
        zero_count = 0
        attached += 1
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 0:
                zero_count += 1
                continue
            if board[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))

        if board[x][y] - zero_count != 0:
            board[x][y] -= zero_count
        else:
            board[x][y] = -1

    return attached


N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 빙산 위치 받음

ice = []
for i in range(N):
    for j in range(M):
        if board[i][j]:
            ice.append((i, j)) # 처음 빙산 위치 저장

c = 0
while True:
    new_ice = []
    if len(ice) == 0:
        c = 0
        break
    a = bfs()
    if len(ice) != a:
        break
    for (x, y) in ice:
        if board[x][y] < 0:
            board[x][y] = 0
        else:
            new_ice.append((x, y))

    ice = new_ice[:]
    c += 1

print(c)


#################################################################
# 내 풀이 파이썬, pypy 둘다 통과 x

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def dfs(x, y, day): # 하룻동안 빙산 녹는 과정만 포함
#     # ice : 녹은 후 남은 빙산, sum_g : graph 합을 구하기 위한 list, visied : 방문 여부, x1, y1 다음 날 빙산 시작을 위해 남은 것 중 하나
#     global ice, sum_g, visited ,x1, y1, day_out
#     # 상0 우1 하2 좌3
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]

#     for k in range(4): # 빙산 한칸 녹이기
#         nx, ny = x+dx[k], y+dy[k]
#         if 0 <= nx < N and 0 <= ny < M:
#             if graph[nx][ny] == 0: # 주변이 0 일 때 <- 녹음
#                 graph[x][y] -= 1
#                 if graph[x][y] <=0: # 빙산이 0보다 작을 경우 일단 * 표시, 0 일경우 옆 빙산 녹을 때 영향끼침
#                     graph[x][y] = '*'
#                     break
#     # 현재 빙산이 남아있는 경우(>0) 남은 빙산 높이 저장                
#     if graph[x][y] != '*' and graph[x][y] > 0:
#         ice.append(graph[x][y])
#         x1, y1 = x, y
#     # 옆 빙산 이동
#     for k in range(4): 
#         nx, ny = x+dx[k], y+dy[k]
#         if 0 <= nx <N and 0 <= ny < M:
#             if graph[nx][ny] != 0 and graph[nx][ny] != '*' and visited[nx][ny] == 0: # *은 하루동안 0 이하가 되어 없어진 빙하. 옆 빙하가 이 빙하를 count 하지 않기 위해
#                 visited[nx][ny] = 1
#                 dfs(nx,ny, day) # 0이 아닌 옆 빙산 탐색

#     # *으로 해놨던 녹은 빙산을 0으로 처리
#     for p in range(N):
#         for q in range(M):
#             if graph[p][q] == '*':
#                 graph[p][q] = 0
    
#     day_out = day

# N, M = map(int, input().split())
# ice = [] # 하룻동안 녹고 난 빙산의 높이들
# graph = [] # 빙산 위치 높이 정보
# sum_g = [] # graph합을 구하기 위해 만듦
# day_out = 0 # 일 수
# x1, y1 = 0, 0 # 빙산 스타트
# visited = [[0]* M for _ in range(N)]
# for i in range(N):
#     graph.append(list(map(int, input().split())))

# t = []
# # 첫 스타트 포인트 하나만 찾음 (한 덩어리 이므로)
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] != 0:
#             t.append([i,j])
#             break
#     if len(t):
#         break
# visited[t[0][0]][t[0][1]] = 1
# # 첫 날
# dfs(t[0][0],t[0][1], day_out)
# # 그 다음 부터
# while True:
#         # 빙산이 2개로 쪼개지면 합이 다름
#     for l in range(N):
#         sum_g.append(sum(graph[l]))
    
#     if sum(ice) != sum(sum_g): # 그날 녹고 난 후 남은 빙산의 높이 합 , graph의 남은 빙산의 높이 합. 같으면 한 덩어리 다르면 두 덩어리
#         print(day_out)
#         break
#     # 하루 지난 후
#     if sum(sum_g) != 0:
#         ice = []
#         sum_g = []
#         visited = [[0]* M for _ in range(N)] # 방문했던 빙산 초기화
#         visited[x1][y1] = 1 # 다 녹지 않고 남은 빙산 x1, y1
#         dfs(x1,y1, day_out+1)
#     else: # graph가 다 0인 경우
#         print(0)
#         break

###############################################################################################
###재윤 풀이 pypy만 통과 가능


from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

glacier = []
for _ in range(N):
    glacier.append(list(map(int, sys.stdin.readline().split())))

#상0 우1 하2 좌3
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 주변에 물이 몇개인지
def count_water(x,y):
    count = 0
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<= nx < N and 0 <= ny < M and glacier[nx][ny] ==0:
            count+=1
    return (x,y,count)

# dfs를 이용하여, 이어진 land를 탐색


    

# bfs를 이용하여, 이어진 land를 탐색

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    checker[x][y] =1
    
    while queue:
        p, q = queue.popleft()

        for i in range(4):
            nx, ny = p+dx[i], q+dy[i]
            if 0<= nx < N and 0 <= ny < M and glacier[nx][ny] > 0:
                if checker[nx][ny] ==0:
                    checker[nx][ny] =1
                    queue.append((nx,ny))


glacier_count = 1 
count = 0 # 땅 덩어리
year = 0

melting_list = []

# 이어진 land가 2개 이상이거나, land가 0개라면 종료
while count < 2 and glacier_count > 0:
    glacier_count = 0
    count = 0
    checker = [[0]* M for _ in range(N)]
# 이어진 땅 덩어리 탐색
    for p in range(N):
        for q in range(M):
            if checker[p][q] == 0 and glacier[p][q] > 0:
                glacier_count += 1
                bfs(p,q)
                count += 1

# 땅이 두개 이상이면 종료
    if count > 1:
        break

# 각 지점의 melting 되는 양을 담아두고 한번에 처리
    for i in range(N):
        for j in range(M):
            if glacier[i][j] != 0:
                melting_list.append(count_water(i,j))
    while melting_list:
        x, y, melt = melting_list.pop()
        glacier[x][y] -= melt
        if glacier[x][y] <0:
            glacier[x][y] =0
    year += 1

if count < 2:
    print(0)
else:
    print(year)



