## 실패 비트마스크 알아야 함

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
queue = []
C = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    for _ in range(c):
        queue.append((a,b))
        C +=1

dp_bag = [[0]*(M+1) for _ in range(C+1)]

for i in range(1, C+1):
    w, v = queue.pop()
    for j in range(1, M+1):
        if j < w:
            dp_bag[i][j] = dp_bag[i-1][j]
        else:
            dp_bag[i][j] = max(dp_bag[i-1][j], v + dp_bag[i-1][j-w])

print(dp_bag[C][M])