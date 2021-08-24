from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y,iceberg,check):
    queue = deque()
    queue.append([x,y])
    check[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(len(dx)):
            nx,ny = x+dx[i], y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if check[nx][ny] ==0 and iceberg[nx][ny] !=0:
                    check[nx][ny] =1
                    queue.append([nx,ny])
def melting(x,y,iceberg,check):
    check[x][y]=1
    for i in range(len(dx)):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if iceberg[nx][ny] ==0 and iceberg[x][y]>0 and check[nx][ny]==0:
                iceberg[x][y]-=1
    if check[x][y]>0:
        return 1
    else:
        return 0
    
n, m = map(int, input().strip().split())

iceberg =[]

for i in range(n):
    iceberg.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

year =0
while True:
    
    flag =0
    
    check=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j]!=0:
                if melting(i,j,iceberg,check):
                    flag=1
                    
                    
    if flag==0:
        year=0
        break
        
    check=[[0 for i in range(m)] for j in range(n)]
    count =0
    
    for i in range(n):
        for j in range(m):
            if check[i][j] ==0 and iceberg[i][j]!=0:
                bfs(i,j,iceberg,check)
                count+=1
                
    if count>=2:
        year+=1
        break
        
    else:
        year+=1
        
print(year)        