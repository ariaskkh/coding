# import sys
# input = sys.stdin.readline

# string = list(input().strip())
# cursor = len(string)
# string.insert(0, '+')
# print(string)

# M = int(input().strip())
# p = 0

# for _ in range(M):
#     x = input().split()
#     # print(x)
#     if x[0] == 'L':
#         if cursor != 0:
#             cursor -= 1
#     elif x[0] == 'D':
#         if cursor != M+p:
#             cursor += 1
#     elif x[0] == 'B':
#         if cursor != 0:
#             del string[cursor]
#             cursor -= 1
#             print(string, 'B')
#     else: ## P인 경우
#         string.insert(cursor+1, x[1])
#         cursor += 1
#         p += 1
#         print(string, 'P')

# print(''.join(string[1:]))


##################################################################
##스택을 이용한 풀이

import sys
input = sys.stdin.readline

stack = list(input().strip())
stack2 = []
M = int(input().strip())

for _ in range(M):
    x = input().split()
    
    if x[0] == 'L' and len(stack) != 0:
        stack2.append(stack.pop())
    elif x[0] == 'D' and len(stack2) != 0:
        stack.append(stack2.pop())
    elif x[0] == 'B' and len(stack) != 0:
        stack.pop()
    elif x[0] == 'P': ## P 문자 왼쪽 추가
        stack.append(x[1])
for i in stack:
    print(i, end="")
for j in range(len(stack2)):
    print(stack2.pop(), end="")