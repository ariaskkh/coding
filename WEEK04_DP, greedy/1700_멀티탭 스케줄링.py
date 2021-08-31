import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 멀티탭과, 전기 용품
multitap = []
electric = list(map(int, input().split()))
for i in range(N):
    multitap.append(electric[i])

# for i in range(2, len(electric)):
#     if electric[i] in multitap:
#         continue
#     idx = 0
#     for j in range(1,len(multitap)):
#         if electric[i:].count(multitap[0]) > electric[i:].count(multitap[j]):
#             idx = j
#         elif electric[i:].count(multitap[0]) == electric[i:].count(multitap[j]):
#             if bisect.bisect_left(electric[i:], multitap[0]) < bisect.bisect_left(electric[i:], multitap[j]):
#                 print(bisect.bisect_left(electric[i:], multitap[0]))
#                 print(bisect.bisect_left(electric[i:], multitap[1]))
#                 idx = j
#     multitap[idx] = electric[i]
#     cnt +=1

cnt = 0
idx = []

# 전체 전기 용품들
for i in range(2, len(electric)):
    if electric[i] in multitap:
        continue
    # 멀티탭 원소들 비교
    J = 0
    for j in range(len(multitap)):
        if multitap[j] in electric[i:]:
            if electric[i:].index(multitap[j]) > J:
                J = electric[i:].index(multitap[j])
                if j == len(multitap):
                    multitap[J] = electric[i]
                    cnt +=1
        # 멀티탭의 원소 중 electric의 i 이후 리스트에 포함되어 있지 않다면 electric[i]원소를 그 자리에 넣음
        else: 
            multitap[j] = electric[i]
            cnt +=1
            break

if N == 1:
    print(K-1)
else:
    print(cnt)
