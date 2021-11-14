import sys
input = sys.stdin.readline

x, y = input().split()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A+B
C.sort()
for j in C:
    print(j, end=" ")