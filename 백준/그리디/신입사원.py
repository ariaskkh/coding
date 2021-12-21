import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    m = int(input().strip())
    arr = [list(map(int,input().split())) for _ in range(m)]
    arr.sort()
    # print(arr)
    cnt =1
    tmp = arr[0][1]
    for i in range(1, len(arr)):
        if tmp > arr[i][1]: # arr[i][1]이 더 낮아야 함
            cnt +=1
            tmp = arr[i][1]
    print(cnt)
    cnt = 0

