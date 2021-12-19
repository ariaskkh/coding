# from collections import deque
# import sys
# input = sys.stdin.readline

# def dfs(v):
#     global cnt
#     visited[v] = True
#     cnt += 1
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)

# n = int(input().strip())
# m = int(input().strip())
# cnt = 0
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# dfs(1)
# print(cnt-1)

########################################################################
## visited와 cnt를 합친 더 간단한 풀이

# import sys
# input = sys.stdin.readline

# def dfs(i):
#     visited[i] = 1
#     for k in graph[i]:
#         if not visited[k]:
#             dfs(k)

# n = int(input().strip())
# kinds = int(input().strip())

# graph = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# for i in range(1,kinds+1):
#     x,y = map(int,input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# dfs(1)
# print(sum(visited)-1)


########################
# 다시 풀이

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global cnt
    visited[start] = 1
    queue = deque([start])
    while (queue):
        x = queue.popleft()
        for j in graph[x]:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                cnt +=1
                

n = int(input().strip())
m = int(input().strip())
# 간선 연결 리스트
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
print(cnt)