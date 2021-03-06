from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    t = [] # 익은 토마토
    t1 = 0 # 안 익은 토마토
    cnt = 0 # 지나간 분
    queue = deque()
    for Z in range(H):
        for X in range(N):
            for Y in range(M):
                if tomato[Z][X][Y] == 1:
                    t.append([Z,X,Y])
                elif tomato[Z][X][Y] == 0:
                    t1 += 1
    if t1 == 0:
        print(0)
        return     
    
    for T in t: # 익은 토마토들
        zz, xx, yy = T[0], T[1], T[2]
        queue.append((zz,xx,yy))
        tomato[zz][xx][yy] == 2 # 2는 지나간 자리
    while queue:
        for _ in range(len(queue)): # 하루에 익은 토마토들 전부 계산을 위해 반복문
            z, x, y = queue.popleft()
            for d in range(6):
                nz, nx, ny = z+dz[d], x+dx[d], y+dy[d]
                if 0<= nz < H and 0<= nx < N and 0<= ny < M:
                    if tomato[nz][nx][ny] == 0:
                        tomato[nz][nx][ny] = 2
                        queue.append((nz,nx,ny))
                        t1 -= 1 # 안익은 토마토 개수 하나씩 감소
        cnt +=1 # 그날 다 익은 후 하루씩 지남

    if t1: # 안 익은 토마토 남아있는 경우
        print(-1)
        return
                    
    print(cnt-1) # 다 익고 난 후 append 된거를 그 다음날까지 진행되므로 1 빼줘야함

#상0 우1 하2 좌3 위4 아래5
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0 ,-1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split()) # M 가로(y), N 세로(x), H 높이(z)
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
bfs()