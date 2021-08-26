# ## 탑다운 방식. 재귀 사용
import sys

input = sys.stdin.readline

N = int(input())
dp =[0] *100
# 피보나치 함수를 재귀함수로 구현, 탑다운 디피
def fibo(x):
    # 종료 조건(1 혹은 2일 때 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo(N))

########################################################################
## 바텀 업 방식

import sys
input = sys.stdin.readline

N = int(input())
# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
dp = [0] * 91
dp[1] = 1
dp[2] = 1
# 피보나치 함수 반복문으로 구현, 바텀업 디피
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])