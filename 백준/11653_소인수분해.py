import sys
input = sys.stdin.readline

n = int(input())
arr = []

if n != 1:
    i = 2
    while(i < n+1):
        while(1):
            if n % i == 0:
                arr.append(i)
                n = n // i
            else:
                i += 1
                break
for j in range(len(arr)):
    print(arr[j])

############################################################

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