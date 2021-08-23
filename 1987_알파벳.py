import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y, cnt):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    global mmax
    mmax = max(mmax, cnt)
    for i in range(4):
        nx, ny = x+ dx[i], y+dy[i]
        if 0<= nx < R and 0<= ny < C and visited[graph[nx][ny]] != 1:
            visited[graph[nx][ny]] = 1
            dfs(nx, ny, cnt +1)
            visited[graph[nx][ny]] = 0

#상0 우1 하2 좌3

R, C = map(int, input().split())
graph = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
mmax = 0
visited = [0] * 26
visited[graph[0][0]] = 1

dfs(0,0, 1)
print(mmax)