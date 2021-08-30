# ## 0부터 증가하는 상향식 1

# import sys
# input = sys.stdin.readline

# x = int(input().strip())

# dp = [10**7]* (3*x+1)
# dp[0],dp[1] = 0,0

# for i in range(1,x+1):

#     dp[3*i] = min(dp[3*i], dp[i]+1)
#     dp[2*i] = min(dp[2*i], dp[i]+1)
#     dp[i+1] = min(dp[i+1], dp[i]+1)

# print(dp[x])


################################################
# 0부터 증가하는 상향식 2, 메모리가 더 적게 씀

import sys
input = sys.stdin.readline

x = int(input().strip())

dp=[None] * (x+1)
dp[1] = 0

for i in range(2,x+1):
    min_v = float("inf")
    if dp[i//2] != None and i % 2 == 0:
       min_v = min(min_v, dp[i//2]+1)
    if dp[i//3] != None and i % 3 == 0:
       min_v = min(min_v, dp[i//3]+1)
    min_v = min(min_v, dp[i-1]+1)
    dp[i] = min_v

print(dp[x])
###########################################################################
## 자헌이 형 하향식. 메모리 초과 뜸

import sys
N = int(sys.stdin.readline())
sys.setrecursionlimit(10**8)
memo = [None] * (N+1)

def fn_topdown(x):
    if memo[x]:
        return memo[x]
    if x == 1:
        return 0
    min_v = float("inf")
    # subproblems = [] # 현재 문제 x의 부분문제들
    if x%3 == 0: min_v = min(min_v, fn_topdown(x//3)+1)
    
    if x%2 == 0: min_v = min(min_v, fn_topdown(x//2)+1)
    min_v = min(min_v, fn_topdown(x-1)+1)
    memo[x] = min_v
    
    return memo[x]
print(fn_topdown(N))