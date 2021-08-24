from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def bfs(a,b):
    global mmax, cnt
    #상0 우1 하2 좌3
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    # 순서 상관없이 있는지 여부만 확인하면 되므로 set으로 진행. queue로 할 경우 시간초과
    queue = set()
    queue.add((a,b,cnt,graph[a][b]))
    while queue:
        x, y, cnt1, before_visit = queue.pop()
        # 네 방향 확인
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in before_visit: # 지금까지의 안 나온 알파벳이여야함
                queue.add((nx,ny, cnt1+1, before_visit+graph[nx][ny]))
                mmax = max(mmax, cnt1+1) 
        
    print(mmax)

R, C = map(int, input().split())
graph = []
for i in range(R):
    graph.append(list(input().strip()))
mmax = 1
cnt = 1

# (0,0 시작)
bfs(0,0) 