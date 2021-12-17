import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
# cnt = 0
ans = []
tmp = arr[0]

for i in range(1, len(arr)):
    if tmp[1] >= arr[i][0]:
        if tmp[1] >= arr[i][1]:
            tmp = arr[i]
    else:
        # print(tmp)
        # cnt += 1
        ans.append(tmp)
        tmp = arr[i]
ans.append(tmp)
print(ans)
print(len(ans))