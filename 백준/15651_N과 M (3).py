import sys
input = sys.stdin.readline
from itertools import product

n, m = list(map(int, input().split()))

for arr in product(range(1,n+1), repeat = m):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()