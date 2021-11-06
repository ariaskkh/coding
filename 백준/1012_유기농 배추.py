## bfs
## Map[nx][ny] =2 인데, ==라고 써서 시간 많이 씀.....
import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(M,N,i,j):
    # global M, N
    queue = deque()
    queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if Map[nx][ny] == 1:
                    queue.append((nx,ny))
                    Map[nx][ny] = 2

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    Map = [[0] * (M) for _ in range(N)]
    cnt = 0

    for _ in range(K):
        y, x = map(int, input().split())
        Map[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if Map[i][j]  == 1:
                Map[i][j] = 0
                bfs(M,N,i,j)
                cnt +=1
    print(cnt)