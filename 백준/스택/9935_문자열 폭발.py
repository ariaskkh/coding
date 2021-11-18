## 첫 풀이 - 시간초과
import sys
input = sys.stdin.readline
string = input().strip()
bomb = input().strip()
tmp = string
tmp1 =''
i = 0
while(len(tmp) != 0):
    tmp = tmp.split(bomb)
    tmp = ''.join(tmp)
    if tmp1 == tmp:
        break
    tmp1 = tmp
if len(tmp) != 0:
    print(tmp)
else:
    print('FRULA')


############################################
## 스택을 이용한 풀이
import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()

stack = []
for i in range(len(string)):
    stack.append(string[i])
    
    if len(stack) >= len(bomb):
        tmp = "".join(stack[-len(bomb):])
        if tmp == bomb:
            cnt = 0
            while cnt < len(bomb):
                stack.pop()
                cnt +=1
if len(stack) != 0:
    print("".join(stack))
else:
    print('FRULA')