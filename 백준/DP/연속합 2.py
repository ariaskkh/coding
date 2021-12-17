### 시간초과
import sys
input = sys.stdin.readline

n = int(input().strip())
DP = list(map(int, input().split()))
DPtmp = DP[:]
minus = []
ans = []
for j in DP:
    if j < 0:
        minus.append(j)

for i in range(1,len(DP)):
    if DP[i-1] >0:
        DP[i] = DP[i] + DP[i-1]
ans.append(max(DP))

for k in minus:
    DP1 = DPtmp[:]
    DP1.remove(k)
    
    for p in range(1,len(DP1)):
        if DP1[p-1] >0:
            DP1[p] = DP1[p] + DP1[p-1]
    ans.append(max(DP1))
print(max(ans))
    

import sys
input = sys.stdin.readline

n = int(input().strip())
DP = list(map(int, input().split()))
DPtmp = DP[:]
minus = []
ans = []
for j in DP:
    if j < 0:
        minus.append(j)

for i in range(1,len(DP)):
    if DP[i-1] >0:
        DP[i] = DP[i] + DP[i-1]
ans.append(max(DP))

for k in minus:
    DP1 = DPtmp[:]
    # print(DP1, k, minus)
    DP1.remove(k)
    
    for p in range(1,len(DP1)):
        if DP1[p-1] >0:
            DP1[p] = DP1[p] + DP1[p-1]
    ans.append(max(DP1))
# print(ans)
print(max(ans))
    

################################################
