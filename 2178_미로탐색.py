from collections import deque
import sys
input = sys.stdin.readline

# bfs로 풀이
#상 0 우 1 하 2 좌 3
def bfs(x,y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    dist[x][y] = 1
    while queue:
        X, Y = queue.popleft()
        for i in range(4):
            temp_x = X + dx[i]
            temp_y = Y + dy[i]
            if 0 <=temp_x < n and 0 <= temp_y < m:
                if graph[temp_x][temp_y] == 1 and visited[temp_x][temp_y] == 0:
                    queue.append([temp_x,temp_y])
                    visited[temp_x][temp_y] = 1
                    dist[temp_x][temp_y] = dist[X][Y] +1

n, m = map(int, input().strip().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().strip())))
visited = [[0] * (m) for _ in range(n)]
dist = [[0] * (m) for _ in range(n)]

bfs(0,0)
print(dist[n-1][m-1])