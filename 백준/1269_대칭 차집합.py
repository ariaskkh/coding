import sys
input = sys.stdin.readline

x, y = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0
if x > y:
    for elem in A:
        if elem in B:
            cnt += 1
else:
    for elem in B:
        if elem in A:
            cnt += 1
print(x+y-cnt*2)


###############

import sys
input = sys.stdin.readline

x, y = map(int, input().split())

A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B) + len(B-A))