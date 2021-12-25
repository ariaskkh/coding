from collections import deque

def get_smallest_node(n,cost, visited):
    min_v = 1e9
    idx = 0 # 가장 비용이 적은 노드(인덱스)
    for k in range(1,n+1):
        if cost[k] < min_v and not visited[k]:
            min_v = cost[k]
            idx = k
    return idx


def dijkstra(start, end, n, graph):
    cost = [0] + [1e9]*(n)
    visited = [0] * (n+1)
    visited[start] = 1
    cost[start] = 0
    
    for j in graph[start]:
        cost[j[0]] = j[1]
    
    for i in range(1, n): # start 제외하고 n-1 다 비교
        now = get_smallest_node(n, cost, visited)# 가장 작은 비용인 값 구함
        visited[now] = 1
        # 다음 노드에 대해 새로운 경로가 기존 경로보다 싸면 비용 업데이트
        for next in graph[now]:
            new_cost = cost[now] + next[1]
            if new_cost < cost[next[0]]:
                cost[next[0]] = new_cost
    ans = cost[end]
    
    return ans 
        
def solution(n, s, a, b, fares):
    answer = 0
    # 간선 정보
    graph = [[] for _ in range(n+1)]
    minv = 1e9
    
    for fare in fares:
        graph[fare[0]].append((fare[1],fare[2]))
        graph[fare[1]].append((fare[0],fare[2]))
    for ii in range(1, n+1):
        # s 시작, ii 지점 경유, a, b에 각각 도착
        result = dijkstra(s, ii, n, graph) + dijkstra(ii, a, n, graph) + dijkstra(ii, b, n, graph)
        if result < minv:
            minv = result
    return minv


    ################################################
    # heap을 이용한 풀이
    