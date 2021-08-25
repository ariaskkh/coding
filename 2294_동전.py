# 동전들 조합을 늘려가며 개수도 증가시킴. 이 때 이미 만든 수는 계산 제외

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    min_count = 10001
    
    for i in range(n):
        queue.append((coin[i],1)) # 동전 하나씩 queue에 넣음
    
    while queue:
        now_coin, count = queue.popleft()
        for j in coin:
            new_coin = now_coin + j  # 동전 조합 계산 시작, 여기서 count도 1 증가
            
            if new_coin > k or visited[new_coin]:
                continue
                
            if new_coin < k and count +1 < min_count:
                visited[new_coin] = 1
                queue.append((new_coin, count+1))
            elif new_coin == k:
                min_count = min(count + 1, min_count)
    if min_count == 10001:
        min_count = -1
    print(min_count)

n, k = map(int, input().split())
coin = []
visited = [0]*10001
for _ in range(n):
    coin.append(int(input().strip()))

bfs()