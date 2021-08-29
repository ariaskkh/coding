import sys
input = sys.stdin.readline

N = int(input())
TP = [[0]*(N+1)]
for _ in range(N):
    TP.append([0] +list(map(int, input().split())))
dp = [[(0,'')]*(N+1) for _ in range(N+1)]
alpha = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
for i in range(1,N+1):
    for j in range(1,N+1):
            if i == 1:
                dp[i][j] = (TP[i][j], alpha[j])
            else:
                dp[i][j] = (100000000,'')
                for k in range(2, N+1):
                    if k != j and alpha[j] not in dp[i-1][k][1]:
                        if TP[k][j] !=0:
                            if dp[i][j][0] > dp[i-1][k][0] + TP[k][j]:
                                dp[i][j] = (dp[i-1][k][0] + TP[k][j], dp[i-1][k][1] + alpha[j])
for p in range(len(dp)):
    print(dp[p])
print(dp[N][1][0])