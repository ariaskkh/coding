import sys
input = sys.stdin.readline

def fibo(x):
    if x == 1 or x == 2 or x == 3:
        return 1
    if x == 4 or x == 5:
        return 2
    
    if dp[x] != 0:
        return dp[x]
    
    dp[x] = fibo(x-1) + fibo(x-5)
    return dp[x]
    
n = int(input())
for i in range(n):
    dp = [0] * 101
    x = int(input())
    print(fibo(x))