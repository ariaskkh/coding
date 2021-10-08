# def solution(numbers, target):
#     answer = 0
#     sums = [0]
#     for num in numbers:
#         tmp = []
#         for parent in sums:
#             tmp.append(parent + num)    
#             tmp.append(parent - num)
#         sums = tmp
#     for i in sums:
#         if i == target:
#             answer +=1
#     return answer

# numbers = [1,2,3,4,5]
# target = 3

# print(solution(numbers, target))

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx == N):
        if target == value:
            answer += 1
        return
    
    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
    
        