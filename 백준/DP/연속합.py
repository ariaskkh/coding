import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
# tmp = 0 ## i-1번째 까지의 합

for i in range(1, len(arr)):
    if arr[i-1] > 0:
        arr[i] = arr[i] + arr[i-1]
    # else:
        # arr[i] = arr[i-1]
print(arr)
print(max(arr))