## 배열은 틀림, 출력 불가

import bisect
import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = []
dp.append(A[0])
# A[i] 가 dp 리스트 안으로 들어가야 함
for i in range(N):
    if A[i] > dp[-1]: 
        dp.append(A[i])
    # bisect_left 는 리스트에서 왼쪽으로부터 A[i]와 '같거나 이보다 큰' 첫 번 째 원소의 index를 반환
    else:
        idx = bisect.bisect_left(dp, A[i])
        dp[idx] = A[i]
print(len(dp))
print(*dp)
    