import sys
input = sys.stdin.readline

x = input().strip()
X = int(x)
for i in range(X):
    tmp = list(str(i))
    if X == i + sum(map(int, tmp)):
        print(i)
        break



# a = '12345'
# b = list(a)
# print(b)
# c = sum(map(int, b))
# print(c)
