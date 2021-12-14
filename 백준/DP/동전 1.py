import sys
input = sys.stdin.readline

n, k = map(int, input().split())

DP = [0]*(k+1)
DP[0] = 1
coins = [int(input().strip()) for _ in range(n)]

for coin in coins:
    for i in range(coin, k+1):
        DP[i] += DP[i-coin]

print(DP)