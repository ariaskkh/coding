import sys
input = sys.stdin.readline

n = int(input())
string = input().strip()
num = ['1','2','3','4','5','6','7','8','9','0']
hidden = ''
answer = []

i = 0
while(i < len(string)):
    
    if string[i] in num:
        while(i < len(string) and string[i] in num):
            hidden += string[i]
            i += 1
    else:
        if len(hidden) != 0:
           answer.append(int(hidden))
           hidden = ''
        i += 1
if len(hidden) != 0:
    answer.append(int(hidden))
    hidden = ''
print(sum(answer))