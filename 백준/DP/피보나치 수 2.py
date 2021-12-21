import sys
input = sys.stdin.readline

n = int(input().strip())
DP = [0] * (n+2)
DP[0] = 0
DP[1] = 0
DP[0] = 1

for i in range(2,n+2):
    x = DP[i-2] + DP[i-1]
    DP[i] = x
print(DP[-1])