import sys
input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int,input().split()))
cards.sort()

M = int(input().strip())
lists = list(map(int,input().split()))
ans = []

def binary(start, end, target, cards):
    mid = (start+end)//2
    if start <= end:
        if target == cards[mid]:
            ans.append(1)
            return
        if target > cards[mid]:
            start = mid+1
            binary(start, end, target, cards)
        else: ## target <= mid
            end = mid-1
            binary(start, end, target, cards)
    else:
        ans.append(0)


for elem in lists:
    binary(0, N-1, elem, cards)

for i in ans:
    print(i, end=" ")
