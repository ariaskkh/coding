import sys
input = sys.stdin.readline

n = int(input().strip())
tops = list(map(int, input().split()))
stack = []
stack.append((0,tops[0]))
ans = []
ans.append(0)

for i in range(1,n): 
    for j in range(len(stack)-1,-1,-1):
        if stack[j][1] > tops[i]:
            ans.append(stack[j][0]+1)
            stack.append((i, tops[i]))
            break
        else:
            stack.pop()
            
        if j == 0:
            ans.append(0)
            stack.append((i,tops[i]))

for k in range(len(ans)):
    print(ans[k], end=" ")

# print(" ".join(map(str, ans)))