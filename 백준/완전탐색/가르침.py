# import sys
# input = sys.stdin.readline

# x = 'antatica'
# y = 'abcdefghijklmnopqrstuvwxyz'
# alpha = set(y)
# # print(alpha)
# ant = set(x) ## a/c/i/t/n
# arr = []

# N, K = input().split()
# num = int(K) - 5

# for _ in range(int(N)):
#     letters = input().strip()
#     sletters = set(letters)
#     lenl= len(sletters)
#     if  lenl - int(K) < 0:
#         break
#     else:
#         arr.append(sletters - ant)
# print(arr)


        # for alphabet in tmp:
        #     if alphabet in arr:
        #         arr[alphabet] += 1
        #     else:
        #         arr[alphabet] = 1
    # ans = sorted(arr.items(), key=(lambda x:x[1]), reverse =True)
    # tmp2 = ans[:num]



# arr = {'a':1}
# arr['b'] = 2
# arr['b'] += 1
# print(arr)


################################################################################################
## 다른 풀이

import sys
input = sys.stdin.readline

n , k = map(int, input().split())

if k < 5 :
    print(0)
    exit()

elif k == 26:
    print(n)
    exit()

ans = 0
words = [set(input().rstrip()) for _ in range(n)]
learn = [0] * 26
print(words)

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c)- ord('a')] = 1

def dfs(idx, cnt):
    global ans

    if cnt == k -5:
        readcnt = 0
        