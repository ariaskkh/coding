from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global mmin
    queue = deque()
    queue.append(X)
    visit[X] = 0
    while queue:
        now = queue.popleft()
        if now == K:
            mmin = min(mmin, visit[now])
            return mmin
        # +1, *2, -1 경우 각각 처리
        next1 = now + 1
        if 0 <= next1 < 100001 and visit[next1] == 0:
            queue.append(next1)
            visit[next1] = visit[now] + 1
        
        next0 = now * 2
        if 0 <= next0 < 100001 and visit[next0] == 0:
            queue.append(next0)
            visit[next0] = visit[now] + 1
        
        next2 = now - 1
        if 0 <= next2 < 100001 and visit[next2] == 0:
            queue.append(next2)
            visit[next2] = visit[now] + 1

X, K = map(int,input().split()) 

mmin = 100001 # 가장 높은 값 설정
visit = [0] * (100001) # 최대 값 설정
print(bfs())