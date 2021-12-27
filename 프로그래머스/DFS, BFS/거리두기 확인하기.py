## backtracking이 안돼서 틀리는 듯?
from collections import deque

def bfs(p,q, place):
    visited = [[0] * (5) for _ in range(5)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0
    queue = deque()
    visited[p][q] = 1
    queue.append([p,q,cnt])
    while queue:
        x,y,cnt1 = queue.popleft()
        # print(x,y, cnt1, visited)
        cnt1 +=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny] == 0 and place[nx][ny] != "X": # 방문하지 않았고 파티션 아닌 경우
                        if place[nx][ny] == "O": # 빈 테이블
                            visited[nx][ny] = 1
                            queue.append([nx,ny,cnt1])
                        else: # P 사람인 경우
                            if cnt1 <= 2: # 거리가 2이하인 경우. 
                                return False
                            else: # 거리가 3 이상인 경우. ㄱㅊ
                                visited[nx][ny] = 1
                                queue.append([nx,ny,0])
                            
    return True


def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P" :
                if bfs(i,j, place) == False:
                    return False
    return True


def solution(places):
    answer = []
    for place in places: # 5번
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    print(answer)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)


######################################################################################################################################################
# 내 원래 풀이에서의 정답
from collections import deque

def bfs(p,q, place):
    visited = [[0] * (5) for _ in range(5)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0
    queue = deque()
    visited[p][q] = 1
    queue.append([p,q,cnt])
    while queue:
        x,y,cnt1 = queue.popleft()
        # print(x,y, cnt1, visited)
        cnt1 +=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny] == 0 and place[nx][ny] != "X": # 방문하지 않았고 파티션 아닌 경우
                        if place[nx][ny] == "O": # 빈 테이블
                            visited[nx][ny] = 1
                            queue.append([nx,ny,cnt1])
                        else: # P 사람인 경우
                            if cnt1 <= 2: # 거리가 2이하인 경우. 
                                return False
                            else: # 거리가 3 이상인 경우. ㄱㅊ
                                visited[nx][ny] = 1
                                queue.append([nx,ny,0])
                            
    return True


def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if bfs(i,j, place) == False:
                    return False
    return True


def solution(places):
    answer = []
    for place in places: # 5번
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


#############################################################################
# P를 기준으로 아닌거 쳐내는 방식
from collections import deque

def bfs(p,q, place):
    visited = [[0] * (5) for _ in range(5)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    visited[p][q] = 1
    queue.append([p,q,0]) # P를 queue에 넣음
    while queue:
        x,y,cnt1 = queue.popleft()
        cnt1 +=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if place[nx][ny] == "X":
                continue
            if cnt1 > 2:
                continue
            if visited[nx][ny]:
                continue
            if place[nx][ny] == "P":
                return False
            queue.append([nx,ny,cnt1])
            visited[nx][ny] = 1
    return True


def check(place):
    for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if bfs(i,j, place) == False:
                        return False
    return True


def solution(places):
    answer = []
    for place in places: # 5번
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    print(answer)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)

