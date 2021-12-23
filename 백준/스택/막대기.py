import sys
input = sys.stdin.readline

n = int(input())
sticks=[]
stack = []
for i in range(n):
    x = int(input().strip())
    sticks.append(x)

stack.append(sticks[-1])
for j in range(n-1, -1, -1):
    if stack[-1] < sticks[j]:
        stack.append(sticks[j])

print(len(stack))
