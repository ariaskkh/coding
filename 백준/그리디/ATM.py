import sys
input = sys.stdin.readline

N = int(input().strip())
ATM = list(map(int, input().split()))
ATM.sort()
time = []
ans = 0

for i in ATM:
    time.append(i)
    ans += sum(time)

print(ans)