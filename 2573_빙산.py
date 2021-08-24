import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y, day): # 하룻동안 빙산 녹는 과정만 포함
    # ice : 녹은 후 남은 빙산, sum_g : graph 합을 구하기 위한 list, visied : 방문 여부, x1, y1 다음 날 빙산 시작을 위해 남은 것 중 하나
    global ice, sum_g, visited ,x1, y1, day_out
    # 상0 우1 하2 좌3
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4): # 빙산 한칸 녹이기
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0: # 주변이 0 일 때 <- 녹음
                graph[x][y] -= 1
                if graph[x][y] <=0: # 빙산이 0보다 작을 경우 일단 * 표시, 0 일경우 옆 빙산 녹을 때 영향끼침
                    graph[x][y] = '*'
                    break
    # 현재 빙산이 남아있는 경우(>0) 남은 빙산 높이 저장                
    if graph[x][y] != '*' and graph[x][y] > 0:
        ice.append(graph[x][y])
        x1, y1 = x, y
    # 옆 빙산 이동
    for k in range(4): 
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx <N and 0 <= ny < M:
            if graph[nx][ny] != 0 and graph[nx][ny] != '*' and visited[nx][ny] == 0: # *은 하루동안 0 이하가 되어 없어진 빙하. 옆 빙하가 이 빙하를 count 하지 않기 위해
                visited[nx][ny] = 1
                dfs(nx,ny, day) # 0이 아닌 옆 빙산 탐색

    # *으로 해놨던 녹은 빙산을 0으로 처리
    for p in range(N):
        for q in range(M):
            if graph[p][q] == '*':
                graph[p][q] = 0
    
    day_out = day

N, M = map(int, input().split())
ice = [] # 하룻동안 녹고 난 빙산의 높이들
graph = [] # 빙산 위치 높이 정보
sum_g = [] # graph합을 구하기 위해 만듦
day_out = 0 # 일 수
x1, y1 = 0, 0 # 빙산 스타트
visited = [[0]* M for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))

t = []
# 첫 스타트 포인트 하나만 찾음 (한 덩어리 이므로)
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            t.append([i,j])
            break
    if len(t):
        break
visited[t[0][0]][t[0][1]] = 1
# 첫 날
dfs(t[0][0],t[0][1], day_out)
# 그 다음 부터
while True:
        # 빙산이 2개로 쪼개지면 합이 다름
    for l in range(N):
        sum_g.append(sum(graph[l]))
    
    if sum(ice) != sum(sum_g): # 그날 녹고 난 후 남은 빙산의 높이 합 , graph의 남은 빙산의 높이 합. 같으면 한 덩어리 다르면 두 덩어리
        print(day_out)
        break
    # 하루 지난 후
    if sum(sum_g) != 0:
        ice = []
        sum_g = []
        visited = [[0]* M for _ in range(N)] # 방문했던 빙산 초기화
        visited[x1][y1] = 1 # 다 녹지 않고 남은 빙산 x1, y1
        dfs(x1,y1, day_out+1)
    else: # graph가 다 0인 경우
        print(0)
        break