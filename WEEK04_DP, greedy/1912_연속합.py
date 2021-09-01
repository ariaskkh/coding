import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split()))

max_v = -1001

DP = []
for i in range(n):
    max_v = max(max_v+ numbers[i], numbers[i])
    DP.append(max_v)

print(max(DP))