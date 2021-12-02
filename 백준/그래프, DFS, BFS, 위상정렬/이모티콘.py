# ## 최솟값, 최소 경로 문제는 bfs나 dfs !
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# S = int(input().strip())

# def dfs(ans, cnt, clipboard):
#     global checker
#     print(ans, cnt, clipboard)
    
#     if cnt == S:
#         # ans = min(ans, cnt)
#         print()
#         print(cnt)
#         return
#     if cnt >= 2*S or cnt <0:
#         return
#     for i in range(3):
#         if i == 0 and checker == 0: #클립보드 복사
#             print("i=0")
#             clipboard = cnt
#             checker = 1
#             dfs(ans, cnt, clipboard)
#         elif i == 1 and clipboard != 0: # 붙여넣기
#             print("i=1")
#             cnt += clipboard
#             checker = 0
#             dfs(ans, cnt, clipboard)
#         elif i ==2 and cnt >= 0: #w 제거
#             cnt -= 1
#             checker = 0
#             dfs(ans, cnt, clipboard)

            

# checker = 0
# ans = 0
# cnt = 1
# clipboard = 0
# dfs(ans, cnt, clipboard)
# print(ans)


######

from collections import deque

n = int(input())
visited = [[-1]*(n+1) for _ in range(n+1)]
queue = deque()
queue.append((1,0)) # 이모티콘 수, 클립보드 이미티콘 개수
visited[1][0] = 0

while queue:
    s, c = queue.popleft()
    if visited[s][s] == -1:
        visited[s][s] = visited[s][c] + 1
        queue.append((s,s))
    if s+c <= n and visited[s+c][c] == -1:
        visited[s+c][c] = visited[s][c] +1
        queue.append((s+c,c))
    if s >=1 and visited[s-1][c] == -1:
        visited[s-1][c] = visited[s][c] + 1
        queue.append((s-1,c))
answer = -1
for i in range(n+1):
    if visited[n][i] != -1:
        if answer == -1 or answer > visited[n][i]:
            answer = visited[n][i]
print(answer)
# print(visited)