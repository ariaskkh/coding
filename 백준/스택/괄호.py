import sys
input = sys.stdin.readline

n = int(input().strip())

def solution(x):
    stack = []
    i = 0
    while i < len(x):
        if x[i] == "(":
            stack.append('(')
        else: # i == ")"
            if len(stack) != 0:
                stack.pop()
            else:
                return False
        i += 1
    
    if len(stack) == 0:
        return True
    else:
        return False

for _ in range(n):
    X = input().strip()
    
    if solution(X) == False:
        print('NO')
    else:
        print('YES')