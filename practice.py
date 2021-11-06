# import sys
# input = sys.stdin.readline

# n = int(input().strip())
# N = int(n//2)
# visited = [0] * (N+1)
# arr = []

# if n == 2:
#     print(2)
# elif n != 1:
#     num = 2
#     while(num < N+1):
#         if visited[num] == 0 and n % num == 0:
#             while(n%num ==0):
#                 arr.append(num)
#                 n = n//num
#         multiple = 1
#         tmp = num
#         while(tmp <= N):
#             visited[tmp] =1
#             multiple += 1
#             tmp = num*(multiple)
#     for k in range(len(arr)):
#         print(arr[k])



################################################

import sys
input = sys.stdin.readline

n = int(input().strip())
N = int(n//2)
visited = [0] * (N+1)
arr = []

if n != 1:
    num = 2
    while(num < N+1):
        if visited[num] == 0:
            while(1):
                if n % num == 0:
                    arr.append(num)
                    n = n//num
                else:
                    visited[num] = 1
                    num += 1
                    break
    if len(arr) !=0:
        for k in range(len(arr)):
            print(arr[k])
    else: ## 없는 경우 소수이므로 자기자신만 소인수
        print(n)