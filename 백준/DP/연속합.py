import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    if arr[i-1] > 0:
        arr[i] = arr[i] + arr[i-1]
print(max(arr))