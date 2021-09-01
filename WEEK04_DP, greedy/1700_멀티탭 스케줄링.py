# ## 첫 코드
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split()) # N: 멀티탭 구멍 개수, K: 전기 용품 사용횟수
# # 멀티탭과, 전기 용품
# multitap = []
# electric = list(map(int, input().split()))
# i_start = 0
# while len(multitap) != N:
#     if electric[i_start] not in multitap:
#         multitap.append(electric[i_start])
#     i_start += 1
# cnt = 0
# # 전체 전기 용품들
# for i in range(i_start, len(electric)):
#     if electric[i] in multitap:
#         continue
#     # 멀티탭 원소들 비교
#     J = 0 # 멀티탭의 가전들이 electric에서 i이후 가장 큰 index있는 것을 멀티탭에서 뽑음
#     for j in range(len(multitap)):
#         if multitap[j] in electric[i:]:
#             if electric[i:].index(multitap[j]) + i > J:
#                 J = electric[i:].index(multitap[j]) + i
#             if j == len(multitap)-1:
#                 multitap[multitap.index(electric[J])] = electric[i]
#                 cnt +=1
#         # 멀티탭의 원소 중 electric의 i 이후 리스트에 포함되어 있지 않다면 electric[i]원소를 그 자리에 넣음
#         else: 
#             multitap[j] = electric[i]
#             cnt +=1
#             break
# print(cnt)

########################################################################
## 수정 코드

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
multitap = []
electric = list(map(int, input().split()))
cnt = 0

for i in range(K):
    # multitap에 있는 경우 안 꽂음
    if electric[i] in multitap:
        continue
    # multitap 개수가 덜 찼으면 먼저 채움
    if len(multitap) < N:
        multitap.append(electric[i])
        continue
    # multitap이 가득 찼고 다음 전기용품이 멀티텝에 없을 때
    idxs = []
    for j in range(N):
        try:
            idx = electric[i:].index(multitap[j])
        except:
            idx = 101
        idxs.append(idx)
    plug_out = idxs.index(max(idxs))
    multitap[plug_out] = electric[i]
    cnt +=1

print(cnt)