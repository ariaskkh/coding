## 시간 초과

# from collections import deque
# def bfs(board):
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     n = len(board)
#     visited = []
#     queue = deque()
#     minv = 1e9
    
#     queue.append((0,0,visited+[(0,0)],0,0)) # x,y,cnt,방향(처음에 0이니)
    
#     while queue:
#         x,y, visit, cnt, prev_i = queue.popleft()
#         if x == n-1 and y == n-1:
#             minv = min(minv, cnt)
#             continue
#         if cnt >= minv:
#             continue
#         for i in range(4):
#             nx,ny = x+dx[i], y+dy[i]
#             if 0<= nx < n and 0 <= ny < n and board[nx][ny] == 0:
#                 if (nx,ny) not in visit:
                    
#                     if prev_i == i or len(visit) == 1:
#                         queue.append((nx,ny, visit+[(nx,ny)], cnt+100, i))
#                     else: # ii != i:
#                         queue.append((nx,ny, visit+[(nx,ny)], cnt+600, i))
#     return minv
        
# def solution(board):
#     answer = 0
#     answer = bfs(board)
#     return answer


########################################################
# visited table을 만들어 현재값이 더 작으면 갱신후 진행!
# if visited[nx][ny] <= n_cnt-400: 이게 핵심인 문제..
from collections import deque
def bfs(board):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    n = len(board)
    # visited = []
    visited = [[0]*(n) for _ in range(n)]
    queue = deque()
    minv = 1e9
    # queue.append((0,0,visited+[(0,0)],0,0)) # x,y,cnt,방향(처음에 0이니)
    queue.append((0,0,0,-1)) # x,y,cnt,방향(처음에 0이니)
    
    while queue:
        x,y, cnt, prev_i = queue.popleft()
        if cnt >= minv:
            continue
        if (x,y) == (n-1, n-1) and minv > cnt:
            minv = cnt
        
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                # (0,0)이거나 같은 방향인 경우
                if prev_i == i or prev_i == -1:
                    n_cnt = cnt + 100
                else: # 다른 방향인경우
                    n_cnt = cnt + 600
                
                if visited[nx][ny] == 0:
                    queue.append((nx, ny, n_cnt, i))
                    visited[nx][ny] = n_cnt
                else: # 방문한 적이 있음
                    if visited[nx][ny] <= n_cnt-400: # 한 곳에서 방향이 꺾여서 nx,ny에서 역전될 수 있음. 즉 400의 차이까지는 허용 가능해야.
                        continue
                    queue.append((nx, ny, n_cnt, i))
                    visited[nx][ny] = n_cnt
    print(visited)
    return minv
        
def solution(board):
    answer = 0
    answer = bfs(board)
    return answer