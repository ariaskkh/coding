# ## 처음 풀이, 그 이전 3가지 경우를 고려
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# # 작은 돌
# small_stone = [1]*(N+1)
# for _ in range(M):
#     x =int(input().strip())
#     small_stone[x] = 0

# J = int((2*N-1)**(1/2))

# dp = [[0]*(N+1) for _ in range(J+1)]
# dp[1][2] = 1

# for k in range(3,N+1): # 총 이동 거리
#     if small_stone[k] == 0:
#             continue
#     for v in range(1, J+1): # 한 번에 이동하는 거리(속도)
#         min_v = float('inf')
#         if dp[v-1][k-v] != 0 :
#             min_v = min(min_v, dp[v-1][k-v]+1)

#         if k-v > 0 and dp[v][k-v] != 0:
#             min_v = min(min_v, dp[v][k-v]+1)

#         if v+1 <= J and k-v > 0 and dp[v+1][k-v] != 0:
#             min_v = min(min_v, dp[v+1][k-v]+1)

#         if min_v == float('inf'):
#             min_v = 0
#         dp[v][k] = min_v
# ans = []
# for V in range(J+1):
#     if dp[V][N] != 0:
#         ans.append(dp[V][N])
# if not ans:
#     print(-1)
# else:
#     print(min(ans))


########################################################################
## 빠른 풀이, 그 이전 3가지 경우를 고려

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 작은 돌
small_stone = [1]*(N+1)
for _ in range(M):
    x =int(input().strip())
    small_stone[x] = 0

J = int((2*N)**(1/2))

dp = [[10001]*(N+1) for _ in range(J+2)]
dp[0][1] = 0

for k in range(2,N+1): # 총 이동 거리
    if small_stone[k] == 0:
            continue
    for v in range(1, J+1): # 한 번에 이동하는 거리(속도)
        dp[v][k] = min(dp[v][k-v], dp[v-1][k-v], dp[v+1][k-v]) + 1

ans = []
for V in range(J+2):
    if dp[V][N] != 10001:
        ans.append(dp[V][N])
if not ans:
    print(-1)
else:
    print(min(ans))


########################################################################
## 다른 풀이. 가장 빠름. 출력 편의를 위해 x,y축 변경

import sys
input = sys.stdin.readline

N, stone_n = map(int, input().split())

stone_small = set()
for _ in range(stone_n):
    stone_small.add(int(input().rstrip()))

dp  = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]

dp[1][0] = 0
for i in range(2, N+1):
    if i in stone_small:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) +1

ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)

# #############################################################################
# ## 이후 3가지 경우를 고려, 메모리 초과...
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# stone = [1]*(N+1)
# for _ in range(M):
#     x =int(input().strip())
#     stone[x] = 0

# J = int((2*N-1)**(1/2))

# dp = [[0]*(J*N) for _ in range(J+1)]
# dp[1][2] = 1

# for k in range(2, N+1):
#     for v in range(1, J+1):
#         if dp[v][k] == 0:
#             continue
        
        
#         # if v-1>0 and k+(v-1) < N+1:
#         if v-1>0:
#             if dp[v-1][k+(v-1)] == 0:
#                 dp[v-1][k+(v-1)] = dp[v][k]+1
#             dp[v-1][k+(v-1)] = min(dp[v-1][k+(v-1)], dp[v][k]+1)

        
#         if k+v <= N:
#             if dp[v][k+v] == 0:
#                 dp[v][k+v] = dp[v][k]+1
#             dp[v][k+v] = min(dp[v][k+v], dp[v][k]+1)

        
#         if k+(v+1) <= N:
#             if dp[v+1][k+(v+1)] == 0:
#                 dp[v+1][k+(v+1)] = dp[v][k] +1
#             dp[v+1][k+(v+1)] = min(dp[v+1][k+(v+1)], dp[v][k] +1)

# ans = []
# for V in range(J+1):
#     if dp[V][N] != 0:
#         ans.append(dp[V][N])
# if not ans:
#     print(-1)
# else:
#     print(min(ans))