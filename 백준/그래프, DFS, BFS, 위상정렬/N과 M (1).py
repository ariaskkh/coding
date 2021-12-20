## 백트래킹.... 개쩐다

import sys
input = sys.stdin.readline

def bt(x): # x는 개수 index
    if x > m:
        for j in range(1, x):
            print(arr[j], end=' ')
        print()
    else:
        for i in range(1, n+1):
            if visited[i] == 0:
                visited[i] = 1
                arr[x] = i
                bt(x+1)
                visited[i] = 0
                arr[x] = 0

n, m = map(int, input().split())
visited = [0] * (n+1)
arr = [0] * (m+1)
bt(1)