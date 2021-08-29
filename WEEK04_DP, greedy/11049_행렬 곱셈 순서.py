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
        dp_m[i][j] = 2 **31
        for k in range(i, j): # k는 행렬 곱하는(자르는) 위치
            dp_m[i][j] = min(dp_m[i][j], dp_m[i][k] + dp_m[k+1][j] + d[i-1]*d[k]*d[j]) # 점화식

print(dp_m[1][N])