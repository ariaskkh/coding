import sys
input = sys.stdin.readline

n = int(input())
x = list(input().strip())
sum = 0

for num in x:
    sum += int(num)
print(sum)

##################################################################
x = sum(map(int,input()))
print(x)