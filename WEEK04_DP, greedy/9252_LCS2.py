## 기존 강의 보고 짠 코드. 문자열 출력을 위해 계산을 한 번 더 해야함 - 길이 김, 속도는 비슷

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

X = list(map(str, input().strip()))
Y = list(map(str, input().strip()))
lx = len(X)
ly = len(Y)

dp = [[0] * (ly+1) for _ in range(lx+1)] # x 가로, y 세로

for i in range(1, lx+1): # x 세로
    for j in range(1, ly+1): # y 가로
        if i == 0 or j == 0:
            dp[i][j] = 0
            continue
        if X[i-1] == Y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[lx][ly])

# LCS 문자열 출력을 위한 함수
def LCS_str(x1,y1):
    # LCS = 0 인경우 종료
    if dp[x1][y1] == 0:
        return
    # X, Y 리스트의 가장 끝 원소의 값이 같은 경우, 그 문자 result에 저장
    if X[x1-1] == Y[y1-1]:
        result.append(X[x1-1])
        LCS_str(x1-1,y1-1)
    # X, Y 리스트의 가장 끝 원소의 값이 다른 경우, X,Y 리스트에서 마지막 원소를 제외했을 때 LCS가 더 큰 경우로 이동
    else:
        if dp[x1-1][y1] > dp[x1][y1-1]:
            LCS_str(x1-1,y1)
        else:
            LCS_str(x1,y1-1)

result = []
LCS_str(lx,ly)
result.reverse()
print(''.join(result))


###########################################################################
## 수정 코드 - 코드 길이 짧음, DP 테이블에 문자열을 저장

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

print(len(dp[lx][ly]))
print(dp[lx][ly])