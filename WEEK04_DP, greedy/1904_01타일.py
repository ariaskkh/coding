import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**3)
N = int(input())

dp = [0]*(N+3)

dp[1] = 1
dp[2] = 2
if N >=3:
    for x in range(3, N+1):
        dp[x] = dp[x-1] + dp[x-2]
        dp[x] %= 15746

print(dp[N] % 15746)