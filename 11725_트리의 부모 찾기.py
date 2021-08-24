import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(parent):
    for i in graph[parent]:
        t.append([i,parent])
        graph[i].remove(parent)
        dfs(i)

N = int(input().strip())
graph = [[] for _ in range(N+1)]
t = []
visit = []
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(N):
    graph[i].sort()

dfs(1)
t.sort()
for k in range(N-1):
    print(t[k][1])