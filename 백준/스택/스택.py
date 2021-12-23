import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []

def solution(a):
    if a[0] == 'push':
        stack.append(x[1])
    elif a[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif a[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)

for i in range(n):
    x = input().split()
    solution(x)
    