import sys
input = sys.stdin.readline

n = int(input().strip())

DP = [0] * (n+1)
DP[1] = 1
if n>=2:
    DP[2] = 2
if n >= 3:
    for i in range(3, n+1):
        DP[i] = (DP[i-1] + DP[i-2])%15746
print(DP[-1])