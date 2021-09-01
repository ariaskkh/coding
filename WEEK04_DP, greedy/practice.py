import sys
input = sys.stdin.readline

X = list(input().strip())
Y = list(input().strip())
lx = len(X)
ly = len(Y)
# memoization을 위한 리스트, X를 세로 축(x좌표), Y를 가로 축(y좌표)로 생각하면 편함
dp = [[''] * (lx+1) for _ in range(ly+1)] # x 가로, y 세로
# LCS 구하기
for i in range(1, ly+1): # x 세로
    for j in range(1, lx+1): # y 가로
        # X,Y 리스트의 가장 끝 원소가 같은 경우
        if X[j-1] == Y[i-1]: 
            dp[i][j] = dp[i-1][j-1] + Y[i-1]
        # X,Y 리스트의 가장 끝 원소가 다른 경우
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[ly][lx]))