import sys
input = sys.stdin.readline

t = input().strip()

T = t.split('-')
p = []
for i in range(len(T)):
    # print(T[i])
    p.append(T[i].split('+'))
cnt =0
for j in range(len(p)):
    for k in range(len(p[j])):
        if j == 0:
            cnt += int(p[j][k])
        else:
            cnt -= int(p[j][k])
print(cnt)