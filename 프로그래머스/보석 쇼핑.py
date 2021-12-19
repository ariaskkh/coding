## 시간 초과 O(n^2)

# def solution(gems):
#     answer = []
#     answer1 = []
#     tmp = []
#     n = len(gems)
#     m = len(set(gems))
#     end = 0 # index
#     minv = 100000
    
#     for start in range(len(gems)):
#         while len(set(gems[start:end+1])) < m and end < n:
#             end += 1
        
#         if len(set(gems[start:end+1])) == m:
#             answer.append([start+1,end+1])
#         end = start +1
    
#     for i in answer:
#         if i[1]-i[0] < minv:
#             minv = i[1]-i[0]
#             answer1 = i
    
#     return answer1


################################################
## 두 번쨰 시도. O(n)으로 !
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

def solution(gems):
    answer = []
    
    n = len(gems)
    m = len(set(gems))
    # index
    start = 0
    end = 0 
    # 현재 선택된 보석들
    curr = {gems[0]:1}
    
    while start < n or end < n:
        # 종류가 부족한 경우
        if len(curr) < m:
            end += 1
            if end == n:
                break

            
            # if curr[gems[end]] != 0: # 이거 틀림...
            print(curr)
            print(curr.keys())
            print(curr.values())
            if gems[end] in curr.keys():
                curr[gems[end]] += 1
            else:
                curr[gems[end]] = 1
        # 종류가 같은 경우
        else:
            print(curr, gems[start])
            answer.append(([start+1,end+1], end-start))
            curr[gems[start]] -= 1
            
            if curr[gems[start]] == 0:
                del curr[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x :(x[1], x[0]))
    print(answer)
    return answer

solution(gems)