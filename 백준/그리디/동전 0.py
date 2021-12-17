import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input().strip()) for _ in range(N)]
coins.reverse()
cnt = 0

for i in coins:
    if K >= i:
       cnt += K // i
       K %= i
print(cnt)