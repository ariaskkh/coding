from collections import deque
import sys
input = sys.stdin.readline

# remove 써서 없애기
# if (,) in 고슴도치

def bfs(r,c):
    global cnt
    #상0 우1 하2 좌3
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0 ,-1]
    flag = False
    queue = deque()

    for i2 in range(r):
        for j2 in range(c):
            if graph[i2][j2] == 'S': #고슴도치
                queue.append((i2,j2))
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*': # 홍수
                queue.append((i,j))
    
    while queue:
        if flag:
            break
        x, y = queue.popleft() # 홍수 먼저 넣어서 고슴도치보다 홍수가 먼저 pop되어 계산됨
        if graph[x][y] == '*': # 홍수일 때
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == '.' or graph[nx][ny] == 'S': # 옆이 비어있을 때
                        queue.append((nx,ny)) # 빈칸에 홍수 추가 queue
                        graph[nx][ny] = '*' # 빈칸에 홍수 추가
                        
        if graph[x][y] == 'S': # 고슴도치 일때
            for k2 in range(4):
                nx2, ny2 = x+dx[k2], y+dy[k2]
                if 0<= nx2 < r and 0 <= ny2 < c:
                    if graph[nx2][ny2] == '.': # 옆이 비어있을 때
                        queue.append((nx2,ny2)) # 빈칸에 홍수 추가 queue
                        graph[nx2][ny2] = 'S' # 빈칸에 홍수 추가
                        visit[nx2][ny2] = visit[x][y] + 1
                    elif graph[nx2][ny2] == 'D':
                        visit[nx2][ny2] = visit[x][y] + 1
                        print(visit[nx2][ny2])
                        flag = True
                        return
    print('KAKTUS')
    return

r, c = map(int, input().split())

graph = []
cnt = 0
for i in range(r):
    graph.append(list(str(input().strip())))
visit = [[0]*c for _ in range(r)]
bfs(r,c)