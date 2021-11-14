import sys
input = sys.stdin.readline

string = list(input().strip())
i = len(string)
string.insert(0, '+')
print(string)

M = int(input().strip())
p = 0

for _ in range(M):
    x = input().split()
    # print(x)
    if x[0] == 'L':
        if i != 0:
            i -= 1
    elif x[0] == 'D':
        if i != M+p:
            i += 1
    elif x[0] == 'B':
        if i != 0:
            del string[i]
            i -= 1
            print(string, 'B')
    else: ## P인 경우
        string.insert(i+1, x[1])
        i += 1
        p += 1
        print(string, 'P')

print(''.join(string[1:]))
