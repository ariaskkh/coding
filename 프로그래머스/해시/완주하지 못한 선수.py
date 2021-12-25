# ## 시간 초과. 그냥 풀어 봄

# from collections import deque

# def solution(participant, completion):
#     answer = ''
#     for i in participant:
#         # print(i, completion)
#         if i in completion:
#             completion.remove(i)
#             continue
#         else:
#             print(i)
#             answer=i
#             break
        
#     return answer

## 해시 임을 알고 풀기

from collections import deque

def solution(participant, completion):
    answer =0
    hashDict = {}
    sumHash = 0
    for part in participant:
        hashDict[hash(part)] = part # Hash: Paricipant의 dictionary 만들기
        sumHash += hash(part) # Participant의 sum(hash) 구하기
    
    for comp in completion:
        sumHash -= hash(comp)
    
    return hashDict[sumHash]