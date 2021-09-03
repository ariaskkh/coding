import sys
input = sys.stdin.readline

N, K = map(int, input().split())
gem = [0]
for _ in range(N):
    gem.append(list(map(int, input().split())))
bag = [0]
for _ in range(K):
    bag.append(int(input().strip()))
bag.sort() # 작은 무게 넣을 수 있는 가방 부터 채움
ans = 0

for weight in bag[1:]:
    dp = [[[0,'']] * (weight+1) for _ in range(N+1)]

    for i in range(1, N+1):
        w, v= gem[i]
        for j in range(1, weight+1):
            if j < w: # j 최대무게, w : 물건 무게
                dp[i][j] = dp[i-1][j]
            else: # 가방 최대 무게가 물건 무게보다 클 때,
                if dp[i-1][j][0] > v + dp[i-1][j-w][0]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j][0] = v + dp[i-1][j-w][0] # 여기서 오류 생김
                    dp[i][j][1] = str(i) + dp[i-1][j-w][1]
    ans += dp[N][weight][0]
    a = list(map(int,dp[N][weight][1])) # 가방에 넣은 보석들 인덱스 번호
    for p in range(a):
        del gem[p]
print(ans)