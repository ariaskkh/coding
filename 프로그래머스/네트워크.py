######################################################
# bfs 내 풀이
import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, n, computers):
    queue = deque()
    queue.append(i)
    while(queue):
        x = queue.popleft()
        for ny in range(n):
            if computers[x][ny] == 1:
                computers[x][ny] = 2
                computers[ny][ny] = 2
                queue.append((ny))

def solution(n, computers):
    answer = 0
    for i in range(n):
        if computers[i][i] == 1:
            bfs(i,n,computers)
            answer +=1
    return answer

computers = [[1,1,0],[1,1,0],[0,0,1]]
n = 3
print(solution(n,computers))

################################################################
# ## 정답. visited 씀
# def solution(n, computers):
#     answer = 0
#     visited = [0 for _ in range(n)]
    
#     def bfs(i):
#         queue = deque()
#         queue.append(i)
#         while queue:
#             x = queue.popleft()
#             visited[x] = 1
#             for a in range(n):
#                 if computers[x][a] and not visited[a]:
#                     queue.append(a)
                    
#     for i in range(n):
#         if visited[i] == 0 :
#             bfs(i)
#             answer +=1
            
#     return answer