# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(200000)

# def dfs(parent):
#     for i in graph[parent]:
#         t.append([i,parent]) # 자식, 부모 저장
#         graph[i].remove(parent) # 자식 제거 후
#         dfs(i) # 자식을 부모로서 dfs 실행

# N = int(input().strip())
# graph = [[] for _ in range(N+1)] # 연결 정보 리스트
# t = [] # 부모 저장 리스트
# for _ in range(N-1):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
# for i in range(N):
#     graph[i].sort()

# dfs(1)
# t.sort()
# for k in range(N-1):
#     print(t[k][1])

##############################################################################
# 다른 사람 풀이 + remove(메모리 초과 피하기), 제일 빠름

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# N = int(input().strip())

# graph = [[] for _ in range(N+1)]
# parents = [0 for _ in range(N+1)]

# for _ in range(N-1):
#     a, b =map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def dfs(start, graph, parents): # start와 parents는 리스트
#     for i in graph[start]:
#         if parents[i] == 0:
#             parents[i] = start
#             if parents in graph[i]:
#                 graph[i].remove(parents) # 자식 제거 후
#             dfs(i, graph, parents)

# dfs(1, graph, parents)

# for i in range(2, N+1):
#     print(parents[i])

###################################
# 다시 풀기

import sys
input = sys.stdin.readline
from collections import deque

def bfs(root):
    queue = deque()
    queue.append(root)
    parent[root] = root
    while queue:
        x = queue.popleft()
        for child in graph[x]:
            if parent[child] == 0:
                parent[child] = x
                queue.append(child)
    for i in range(2, len(parent)):
        print(parent[i])

n = int(input().strip())
graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)

for _ in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)