import sys
input = sys.stdin.readline

def solution(idx):
    if idx == m+1:
        for j in range(1, idx):
            print(arr[j], end=" ")
        print()
    else:
        for i in range(1, n+1):
            arr[idx] = i
            solution(idx+1)

n, m = map(int, input().split())
arr = [0] * (m+1)
solution(1)