from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    coin_list = deque()
    min_count = 10001
    # for i in range(n-1,-1,-1): # 이거 왜 안됨?
    for i in range(n-1,-1,-1):
        queue.append((coin[i],1))
    
    while queue:
        now_coin, count = queue.popleft()
        for j in coin:
            new_coin = now_coin + j
            
            if new_coin > k:
                break
            if visited[new_coin]:
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

coin.sort() # reverse는 왜 안됨?
bfs()