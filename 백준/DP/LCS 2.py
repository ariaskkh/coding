import sys
input = sys.stdin.readline

n = list(input().strip()) # 가로
m = list(input().strip()) # 세로

LCS = [["" for _ in range(len(n)+1)] for _ in range(len(m)+1)]

for i in range(1, len(m)+1):
    for j in range(1, len(n)+1):
        if m[i-1] == n[j-1]: # 같은 경우
            LCS[i][j] = LCS[i-1][j-1] + n[j-1]
        else: # 다른 경우
            print(i,j)
            print("hihi",LCS[i][1],"j", LCS[i][j])
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
print(len(LCS[len(m)][len(n)]))
print(LCS[len(m)][len(n)])