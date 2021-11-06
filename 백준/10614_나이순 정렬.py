import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    age, name = input().split()
    arr.append((int(age),name,int(i)))

arr.sort(key=lambda x : (x[0], x[2]))
for j in range(len(arr)):
    print(arr[j][0], arr[j][1])