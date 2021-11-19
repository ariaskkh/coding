import sys
input = sys.stdin.readline

x = input().strip()
X = int(x)

cnt = 0
min_x = abs(X-len(x)*9)

if X <= 18:
    for i in range(X):
        tmp = list(str(i))
        if X == i + sum(map(int, tmp)):
            print(i)
            cnt +=1
            break
else:
    for i in range(min_x,X):
        tmp = list(str(i))
        if X == i + sum(map(int, tmp)):
            print(i)
            cnt +=1
            break
if cnt == 0:
    print(0)