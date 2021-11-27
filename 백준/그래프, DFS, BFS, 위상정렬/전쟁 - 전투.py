import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[0]*(N) for _ in range(M)]
arr =[]
cntw=0
cntb=0
ans1 = []
ans2 = []
for _ in range(M):
    arr.append(list(input().strip()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfsw(x,y):
    global cntw, cntb
    if arr[x][y] == 'W' and visited[x][y] == 0:
        visited[x][y] = 1
        cntw +=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] == 'W':
                    dfsw(nx,ny)
def dfsb(x,y):
    global cntw, cntb
    if arr[x][y] == 'B' and visited[x][y] == 0:
        visited[x][y] = 1
        cntb +=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] == 'B':
                    dfsb(nx,ny)

for p in range(M):
    for q in range(N):
        dfsw(p,q)
        if cntw != 0:
            ans1.append(cntw*cntw)
            cntw = 0
        dfsb(p,q)
        if cntb != 0:
            ans2.append(cntb*cntb)
            cntb = 0

print(sum(ans1), end=" ")
print(sum(ans2))