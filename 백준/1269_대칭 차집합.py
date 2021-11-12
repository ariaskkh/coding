# import sys
# input = sys.stdin.readline

# x, y = map(int, input().split())

# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# cnt = 0
# if x > y:
#     for elem in A:
#         if elem in B:
#             cnt += 1

# else:
#     for elem in B:
#         if elem in A:
#             cnt += 1
# print(x+y-cnt*2)

a = [2,1,3]
a.sort()
print(a)