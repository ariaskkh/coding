import sys
input = sys.stdin.readline

n = int(input().strip())
house = []
for _ in range(n):
    house.append(list(map(int,input().split())))
color = [1,2,3]
DP = [[0] * (4) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,4):
        if i != 1:
            color.remove(j)
            DP[i][j] = min(DP[i-1][color[0]], DP[i-1][color[1]]) + house[i-1][j-1]
            color.append(j)
        else: # i == 1:
            DP[i][j] = house[i-1][j-1]

print(min(DP[n][1:]))