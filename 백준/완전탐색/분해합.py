import sys
input = sys.stdin.readline

x = input().strip()
X = int(x)
cnt = 0
for i in range(X):
    tmp = list(str(i))
    if X == i + sum(map(int, tmp)):
        print(i)
        cnt +=1
        break
if cnt == 0:
    print(0)