# 하향식 - 시간 초과

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

#부분 수열의 최장 길이
def LCS(X,Y): # x, y 는 list
    x = len(X)
    y = len(Y)
    if x == 0 or y == 0:
        dp[x][y] = 0
        return dp[x][y]
    #메모이제이션
    if dp[x][y] != 0:
        return dp[x][y]
    if X[-1] == Y[-1]:
        dp[x][y] = LCS(X[:x-1],Y[:y-1]) +1
        return dp[x][y]
    else:
        dp[x][y] = max(LCS(X[:x-1],Y), LCS(X,Y[:y-1]))
        return dp[x][y]

a = list(map(str,input().strip()))
b = list(map(str,input().strip()))
dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
print(LCS(a,b))


################################################################################################
## 상향식

import sys
input = sys.stdin.readline

X = list(map(str, input().strip()))
Y = list(map(str, input().strip()))
x = len(X)
y = len(Y)
# memoization을 위한 리스트, X를 세로 축(x좌표), Y를 가로 축(y좌표)로 생각하면 편함
dp = [[0] * (y+1) for _ in range(x+1)] # x 가로, y 세로
# LCS 구하기
for i in range(0, x+1): # x 세로
    for j in range(0, y+1): # y 가로
        # 빈 리스트의 경우 LCS = 0
        if i == 0 or j == 0: 
            dp[i][j] = 0
            continue
        # X,Y 리스트의 가장 끝 원소가 같은 경우
        if X[i-1] == Y[j-1]: 
            dp[i][j] = dp[i-1][j-1] + 1 
        # X,Y 리스트의 가장 끝 원소가 다른 경우
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 두 경우 중 LCS가 큰 경우의 값을 받음

print(dp[x][y])


###########################################################################
## 수정 코드 - 코드 길이 짧음 LCS2 문제 답

import sys
input = sys.stdin.readline

X = list(input().strip())
Y = list(input().strip())
lx = len(X)
ly = len(Y)
# memoization을 위한 리스트, X를 세로 축(x좌표), Y를 가로 축(y좌표)로 생각하면 편함
dp = [[''] * (ly+1) for _ in range(lx+1)] # x 가로, y 세로
# LCS 구하기
for i in range(1, lx+1): # x 세로
    for j in range(1, ly+1): # y 가로
        # X,Y 리스트의 가장 끝 원소가 같은 경우
        if X[i-1] == Y[j-1]: 
            dp[i][j] = dp[i-1][j-1] + X[i-1]
        # X,Y 리스트의 가장 끝 원소가 다른 경우
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp[lx][ly])