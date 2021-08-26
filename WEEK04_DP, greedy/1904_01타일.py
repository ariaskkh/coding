import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())

dp = [0]*1000001

def fibo(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo(N)%15746)