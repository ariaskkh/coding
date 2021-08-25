# 내 풀이

import sys
input = sys.stdin.readline

def dfs(heavy):
    if graph[heavy]: # 가벼운 구슬이 존재할 때,
        for light in graph[heavy]:
            heavy_list.append(heavy) # 가벼운 구슬(j) 개수만큼 visit 에 무거운 구슬(heavy)에 depth 증가를 위해 저장
            light_list.append(light)
            # graph[heavy].remove(light)
            dfs(light) # 가벼운 구슬로 dfs

        for k in heavy_list: # 무거운 구슬
            visit_h[k] += 1 # 무거운 구슬들 depth 1씩 증가
        for k1 in light_list:
            visit_l[k1] += 1 # 가벼운 구슬들 depth 1씩 증가
        heavy_list.clear()
        light_list.clear()

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)] #O(N*M)
visit_h = [0] * (N+1) # 
visit_l = [0] * (N+1)
heavy_list = [] # 
light_list = []

cnt = 1
for _ in range(M): # O(M)
    x, y = map(int, input().split())
    graph[x].append(y)

for i in range(N): # O(N)
    graph[i].sort()

for i in range(1,N+1): # O(N)
    dfs(i)
    visit_list = []
    heavy_list = []
    light_list = []

cnt =0
for p in range(1,N+1): # O(N)
    if visit_h[p] >= int((N+1)/2):
        cnt +=1
for q in range(1,N+1): # O(N)
    if visit_l[p] >= int((N+1)/2):
        cnt +=1        
print(cnt)

##################################################################
# 다른 사람 풀이
# import sys; INP = sys.stdin.readline

# N, M = map(int, INP().split())
# small = [ [] for _ in range(N+1) ]
# big = [ [] for _ in range(N+1) ]
# for i in range(M):
#     b, s = map(int, INP().split())
#     small[b].append(s)
#     big[s].append(b)

# def smallCnt(n):
#     visited[n] = True
#     cnt = 0
#     for next in small[n]:
#         if visited[next]:
#             continue
#         cnt += 1
#         cnt += smallCnt(next)
#     return cnt

# def bigCnt(n):
#     visited[n] = True
#     cnt = 0
#     for next in big[n]:
#         if visited[next]:
#             continue
#         cnt += 1
#         cnt += bigCnt(next)
#     return cnt

# mid = (N+1) // 2
# ans = 0
# for i in range(1, N+1):
#     visited = [False] * (N+1)
#     if mid <= smallCnt(i) or mid <= bigCnt(i):
#         ans += 1

# print(ans)

################################################################
# 다른 사람 풀이 2
# import sys
# imput = sys.stdin.readline

# N, M = map(int, input().split())
# heavy = [[] for _ in range(N+1)]
# light = [[] for _ in range(N+1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     heavy[b].append(a)
#     light[a].append(b)

# def count(start, graph):
#     cnt = 0
#     visited[start] = 1

#     for next in graph[start]:
#         if visited[next] == 1:
#             continue
#         cnt += 1
#         cnt += count(next,graph)
#     return cnt

# mid = int((N+1)/2)
# ans = 0
# for j in range(1,N+1):
#     visited = [0]*(N+1)
#     if mid <= count(j,heavy) or mid <= count(j,light):
#         ans += 1
# print(ans)