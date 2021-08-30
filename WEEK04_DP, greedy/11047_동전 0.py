import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input().strip()))
coin.reverse()
cnt = 0
for i in range(len(coin)):
    cnt += K//coin[i]
    K = K%coin[i]

print(cnt)