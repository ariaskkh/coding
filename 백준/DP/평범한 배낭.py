import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0,0]]
for _ in range(n):
    bag.append(list(map(int, input().split())))

DP = [[0]* (k+1) for _ in range(n+1)]
print(bag)
for N in range(1,n+1):
    for K in range(1, k+1):
        if K-bag[N][0] < 0:
            DP[N][K] = DP[N-1][K]
        else:
            DP[N][K] = max(DP[N-1][K], DP[N-1][K-bag[N][0]]+bag[N][1])
print(DP[N][K])
            
