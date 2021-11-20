## 아직 안올림

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = input().split()

cards = list(map(int, input().split()))
cards.sort()
ans = []

clist = list(combinations(cards, 3))
for i in clist:
    t = sum(map(int, i))
    if t <= int(M):
        ans.append(t)
print(max(ans))