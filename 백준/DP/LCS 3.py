import sys
input =sys.stdin.readline

x = input().strip()
y = input().strip()
z = input().strip()
## 문자열로 구하기 - 틀림
# LCS = [[["" for _ in range(len(z)+1)] for _ in range(len(y)+1)] for _ in range(len(x)+1)]

# for xx in range(1, len(x)+1):
#     for yy in range(1, len(y)+1):
#         for zz in range(1, len(z)+1):
#             if y[yy-1] == x[xx-1] == z[zz-1]:
#                 LCS[xx][yy][zz] = LCS[xx-1][yy-1][zz-1] + x[xx-1]
#             else: # 마지막 문자들이 다를 경우. 이부분을 max로 하면 숫자가 됨.....
#                 LCS[xx][yy][zz] = max(LCS[xx-1][yy][zz], LCS[xx][yy-1][zz], LCS[xx][yy][zz-1], LCS[xx-1][yy-1][zz], LCS[xx][yy-1][zz-1], LCS[xx-1][yy][zz-1])

# print(len(LCS[-1][-1][-1]))


## 숫자로 구하기 - 맞음
LCS = [[[0 for _ in range(len(z)+1)] for _ in range(len(y)+1)] for _ in range(len(x)+1)]

for xx in range(1, len(x)+1):
    for yy in range(1, len(y)+1):
        for zz in range(1, len(z)+1):
            if y[yy-1] == x[xx-1] == z[zz-1]:
                LCS[xx][yy][zz] = LCS[xx-1][yy-1][zz-1] + 1
            else: # 마지막 문자들이 다를 경우
                LCS[xx][yy][zz] = max(LCS[xx-1][yy][zz], LCS[xx][yy-1][zz], LCS[xx][yy][zz-1], LCS[xx-1][yy-1][zz], LCS[xx][yy-1][zz-1], LCS[xx-1][yy][zz-1])

print(LCS[-1][-1][-1])