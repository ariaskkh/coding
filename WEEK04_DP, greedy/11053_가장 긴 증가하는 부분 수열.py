## 첫 풀이. 리스트도 출력 가능하다

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = [0] # 인덱스 중 j-1이 있기 때문에 처음에 0을 넣어주고 마지막 개수에서 하나 뺌
for i in range(N): # 입력 받은 수열 A 에 대해
    for j in range(len(dp)-1,-1,-1): # dp 리스트를 뒤에서 부터 확인
        if j == len(dp)-1:
            # A 가장 오른쪽 원소(큰값) 보다 A[i]가 더 크면 dp에 추가
            if dp[j] < A[i]: 
                dp.append(A[i])
            # 여기 중요 !
            elif dp[j-1] < A[i] < dp[j]:
                dp[j] = A[i]
        else:
            if dp[j] < A[i] < dp[j+1]:
                dp[j+1] = A[i]
print(len(dp)-1)
print(*dp[1:])


###########################################################################
## 다른 풀이
import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

###########################################################################
## 다른 풀이 2 bisect를 이용해 더 빠름, 하지만 dp에 배열은 틀림... 출력 불가

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