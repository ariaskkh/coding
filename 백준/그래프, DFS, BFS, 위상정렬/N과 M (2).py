import sys
input = sys.stdin.readline

def bt(idx):
    if idx == m+1:
        for j in range(1, m+1):
            print(arr[j], end= " ")
        print()
    else:
        for i in range(1, n+1):
            if visited[i] == 0 and i > arr[idx-1]:
                visited[i] = 1
                arr[idx] = i
                bt(idx+1)
                visited[i] = 0
                arr[idx] = 0
        

n, m = map(int, input().split())
visited = [0] * (n+1)
arr = [0] * (m+1)

bt(1)