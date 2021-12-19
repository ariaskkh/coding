## 더 싼 주유소 나올 때 더해왔던 거리 * 가장 싼 값

# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# roads =  list(map(int,input().split()))
# costs =  list(map(int,input().split()))
# leastp = costs[0]
# dist= 0

# res = roads[0]* costs[0]

# for i in range(1, N-1):
#     if costs[i] < leastp: # 더 싼 가격
#         res += leastp * dist
#         dist = roads[i]
#         leastp = costs[i]
#     else: # 더 비싼 가격
#         dist += roads[i]
#     if i == N-2:
#         res += leastp * dist
# print(res)

        
#############################################
## 한 칸 갈 떄마다 가격 갱신

import sys
input = sys.stdin.readline

N = int(input().strip())
roads =  list(map(int,input().split()))
costs =  list(map(int,input().split()))
leastp = costs[0]
dist= 0
# res = roads[0]* costs[0]
res = 0

for i in range(N-1):
    if costs[i] < leastp: # 더 싼 가격
        leastp = costs[i]
    res += leastp * roads[i]
    
print(res)

    
