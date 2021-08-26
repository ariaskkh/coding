import sys
input = sys.stdin.readline

N = int(input())

# 0과 1이 피보나치 수열로 증가함
cnt0 = [0]*41
cnt0[0] = 1
cnt0[1] = 0
for i in range(2, 41):
    cnt0[i] = cnt0[i-1] + cnt0[i-2]

cnt1 = [0]*41
cnt1[0] = 0
cnt1[1] = 1
for i in range(2, 41):
    cnt1[i] = cnt1[i-1] + cnt1[i-2]

for _ in range(N):
    i = int(input())
    print(cnt0[i], end=' ')
    print(cnt1[i])