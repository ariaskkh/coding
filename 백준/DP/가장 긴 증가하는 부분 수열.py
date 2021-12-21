import sys
input = sys.stdin.readline

x = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(x)]

for i in range(x):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))