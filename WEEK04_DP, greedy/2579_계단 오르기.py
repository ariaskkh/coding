# 처음에 문제 이해를 잘못함...... 한칸 점프를 연속 세 번 못하는줄.

import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0]*(n+1)
stairs = [0]
for _ in range(n):
    stairs.append(int(input().strip()))
print(stairs)

for i in range(1, n+1):
    if i == 1:
        dp[1] = stairs[1]
    elif i == 2:
        dp[2] = stairs[1] + stairs[2]
    elif i == 3:
        dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])
    else:
        dp[i] = max(dp[i-2], dp[i-3]+ stairs[i-1]) + stairs[i]

print(dp[n])