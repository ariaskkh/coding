import sys
input = sys.stdin.readline

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        dp[0][0][0] = 1
        return dp[0][0][0]
    if a > 20 or b > 20 or c > 20:
        dp[20][20][20] = w(20,20,20)
        return dp[20][20][20]
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return dp[a][b][c]
    
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print(f'w({x}, {y}, {z}) = ', end='')
    print(w(x,y,z))