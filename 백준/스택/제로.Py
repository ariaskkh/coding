import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []
for i in range(n):
    x = int(input().strip())
    if x:
        stack.append(x)
    else:
        stack.pop()
print(sum(stack))