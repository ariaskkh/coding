# #진영 풀이
# import sys
# from collections import deque
# input=sys.stdin.readline
# #입력값 받기 
# N=int(input()) #부품 수 N이 완제품
# V=int(input()) #간선 수
# E=[[] for _ in range(N+1)] #연결정보.
# indegree=[0]*(N+1) #부품별 진입차수 0일 경우 기본부품.
# needs=[[0]*(N+1) for _ in range(N+1)] #각 부품이 기본부품 얼마나 필요한지 Matrix

# for i in range(V):
#     a,b,c = map(int,input().split())
#     E[b].append([a,c])  #a만드는데 b가 c개 필요.
#     indegree[a]+=1      #진입차수 정보모음

# q=deque()
# basic_parts=[]
# for i in range(1,N+1):
#     if indegree[i]==0:
#         basic_parts.append(i) #기본부품 리스트
#         q.append(i)

# while q:
#     now=q.popleft()
#     for object, n in E[now]:
#         if now in basic_parts:   # 기본부품일경우 목적제품에 +n개
#             needs[object][now]+=n
#         else:
#             for i in range(1,N+1):
#                 needs[object][i]+=needs[now][i]*n
#         indegree[object]-=1
#         if indegree[object]==0:
#             q.append(object)

# for i in range(N+1):
#     if needs[N][i] > 0:
#         print(i,needs[N][i])

# #위랑 같은 표현
# # for x in enumerate(needs[N]):
# #     if x[1]>0:
# #         print(*x)

# ###########################################################################################
# # 재윤 풀이
# import sys
# import collections
# import heapq


# parts_N = int(sys.stdin.readline().strip())

# M = int(sys.stdin.readline().strip())

# parts_need = [[0] * (parts_N + 1) for _ in range(parts_N + 1)]
# indegree = [0] * (parts_N + 1)

# for _ in range(M):
#     target, part, count = map(int, sys.stdin.readline().strip().split())
#     parts_need[part][target] = count
#     indegree[target] += 1

# queue = []
# basic_part = []
# for i in range(1, parts_N + 1):
#     if indegree[i] == 0:
#         heapq.heappush(queue, i)
#         basic_part.append(i)
# for basic in basic_part:
#     parts_need[basic][basic] = 1


# while queue:
#     start = heapq.heappop(queue)

#     for i in range(1, parts_N + 1):
#         if parts_need[start][i] > 0 and indegree[i] > 0:
#             print(start,i)
#             for basic in basic_part:
#                 parts_need[i][basic] += parts_need[start][basic] * parts_need[start][i]
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 queue.append(i)

# for basic in basic_part:
#     print(basic, parts_need[parts_N][basic])




###########################################################################
# 진영꺼 보고 내가 다시 작성한 풀이
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip()) # 완제품 번호
M = int(input().strip()) # 어떤 부품을 완성하는데 필요한 부품들의 관계 수

indegree= [0]* (N+1) # 진입 차수
parts_graph = [[] for _ in range(N+1)] # 간선 정보 + 필요 파츠 개수 정보
need = [[0] * (M+1) for _ in range(N+1)] # 파츠가 몇개 필요한지에 대한 정보

for i in range(M):
    a,b,c = map(int, input().split()) # a를 만들기 위해 b가 c개 필요
    parts_graph[b].append((a,c)) # 부품 b 인덱스에 만들 a 와 개수 c 저장
    indegree[a] += 1 # a가 만들어지는 것이므로 a가 진입 차수 증가

queue = deque()
basic_parts = [] # 기본 부품 리스트
for i in range(N+1):
    if indegree[i] == 0:
        basic_parts.append(i) # 기본 부품 리스트 추가_ 0,1,2,3,4 들어감
        queue.append(i)

while queue:
    now = queue.popleft()
    for (object,count) in parts_graph[now]:
        if now in basic_parts: # now가 기본 parts일때
            need[object][now] = count # 기본 부품일 때는 그냥 count
        else: # now가 중간, 완제품일때
            for i in range(N+1): # 모든 기본 부품들을 다 계산해야하므로 반복문
                need[object][i] += need[now][i] * count #obejct: 만들어 지는 부품, now: 만드는,재료 부품
        indegree[object] -=1 # 진입 차수 감소
        if indegree[object] ==0: # 진입 차수 0이면
            queue.append(object) # queue에 추가

for i in range(1,N+1):
    if need[N][i]: # 완제품의 기본제품들
        print(i, need[N][i])