import sys
input = sys.stdin.readline

def dfs(i):
    global cnt
    if graph[i]:
        for j in range(len(graph[i])):
            x = graph[i][j]
            cnt +=1
            dfs(x)
    
    
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visit = []
cnt = 1
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

for i in range(N):
    graph[i].sort()

for i in range(1,N+1):
    result = dfs(i)
    print(cnt)
    cnt =1
    # if result >= int((N+1)/2):
    #     print(i)