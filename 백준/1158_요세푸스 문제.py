## 내 풀이

import sys
input = sys.stdin.readline
from collections import deque

# n, k = map(int, input().strip().split())

# queue = deque()
# for i in range(1,n+1):
#     queue.append(i)
# visited = [0] * (n+1)
# p = k
# ans = []
# while (len(ans) != len(queue)):
#     cnt = 0
#     if visited[p] == 0:
#         visited[p] = 1
#         if p != 0:
#             ans.append(p)
#         else:
#             ans.append(n)
    
#     while(cnt != k and sum(visited) != n):
#         p += 1
#         p = p % n
#         if visited[p] == 0:
#             cnt += 1
#     cnt = 0
# print(ans)

################################################################################

n, k = map(int, input().strip().split())
circular_list= []
ans = []

for i in range(1,n+1):
    circular_list.append(i)

p = 0


while len(circular_list) > 0:
    # print("p :",p,"ans :", ans, "circular_list :", circular_list)
    p = (p + (k-1)) % len(circular_list)
    pop_elem = circular_list.pop(p)
    ans.append(pop_elem)

print("<",end="")
for i in range(n-1):
    print(ans[i],end=", ")
print(ans[-1],end="")
print(">",end="")
