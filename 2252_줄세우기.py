from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N : 사람 수, M: 연결 수
indegree = [0] * (N+1) # 차수
graph = [[] for i in range(N+1)] # 연결 리스트
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # a가 아니라 b의 차수가 증가!

def topological_sort(): # 위상 정렬
    result = []
    queue = deque()
    for k in range(1,N+1): # 차수 0인 것 queue에 넣기
        if indegree[k] == 0:
            queue.append(k)
    while queue:
        x = queue.popleft()
        result.append(x) # 차수 0인 것 queue에서 뺴서 result에 append
        for i in graph[x]:
            indegree[i] -= 1 # 차수 0인 것과 연결된 것 차수 1씩 감소
            if indegree[i] ==0: # 감소 후 차수 0인 것 새로 생기면 queue에 append
                queue.append(i)
    for i in result:
        print(i, end= ' ')
    
topological_sort()