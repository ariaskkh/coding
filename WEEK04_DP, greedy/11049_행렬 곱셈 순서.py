# 행복은 곱셈 순서가 아니잖아요!

import sys
input = sys.stdin.readline
d = [] # 행렬들 저장
N = int(input().strip())
# 행렬들 저장
for i in range(N):
    x,y  = map(int, input().split())
    if i == 0:
        d.append(x) # 첫 행렬 원소만 행과 열 다 입력
    d.append(y) # 이후 열만 입력

dp_m = [[0]*(N+1) for _ in range(N+1)]
# 점화식을 먼저 세우고 변수를 넣어주는 것이 좋음
for r in range(1,N+1): # x축 다 움직인 후, y축 움직이기 위헤 r 도입
    for i in range(1,N-r+1): # x축
        j = i + r # y축
        dp_m[i][j] = 2 ** 31
        for k in range(i, j): # k는 행렬 곱하는(자르는) 위치
            dp_m[i][j] = min(dp_m[i][j], dp_m[i][k] + dp_m[k+1][j] + d[i-1]*d[k]*d[j]) # 점화식
            print(i,j,k)
print(dp_m[1][N])


##############################################################################
# diagonal 출력을 위한 반복문 만들기

# # i와 j가 1씩 차이나게 출력
# N = 4
# for i in range(1, N+1):
#     j =  i + 1
#     print(i,j)
# # 1 2
# # 2 3
# # 3 4
# # 4 5

# # i가 다시 1부터 반복하기 위해 반복문 추가
# N = 4
# for r in range(1, N+1):
#     for i in range(1, N+1):
#         j = i + 1
#         print(i,j)
# # 1 2
# # 2 3
# # 3 4
# # 4 5
# # 위가 총 4번 출력

# # r이 증가할수록 i가 감소해야 한다
# N = 4
# for r in range(1, N+1):
#     for i in range(1, N+1-r):
#         j = i + 1
#         print(i,j)

# # 1 2
# # 2 3
# # 3 4
# # 1 2
# # 2 3
# # 1 2

# # i가 증가할 때 j의 값을 증가시킨다.
# N = 4
# for r in range(1, N+1):
#     for i in range(1, N+1-r):
#         j = i + r
#         print(i,j)

# # 1 2
# # 2 3
# # 3 4
# # 1 3
# # 2 4
# # 1 4