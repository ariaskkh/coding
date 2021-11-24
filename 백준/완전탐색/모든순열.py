import sys
from itertools import permutations
input = sys.stdin.readline


N = int(input().strip())
arr = []

for i in range(1, N+1):
    arr.append(i)

y = list(permutations(arr, N))

for out in y:
    for j in out:
        print(j, end=" ")
    print()