import sys
input = sys.stdin.readline

def dfs(x,y):
    global cnt
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = 1
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] ==1 and visited[nx][ny] == 0:
                cnt +=1
                dfs(nx,ny)

N = int(input().strip())
visited = [[0] *(N+1) for _ in range(N+1)]

graph = []
for _ in range(N):
    graph.append(list(map(int,input().strip())))
cnt = 1    
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            ans.append(cnt)
            cnt = 1
ans.sort()
print(len(ans))
for q in range(len(ans)):
    print(ans[q])