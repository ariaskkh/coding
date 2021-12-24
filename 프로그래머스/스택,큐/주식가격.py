# def bfs(start, prices):
#     print(start)
#     queue = deque()
#     queue.append((prices[start],0, 0))
#     ans = []
#     while queue:
#         x, cnt, idx = queue.popleft()
#         cnt += 1
#         idx += 1
#         if idx < len(prices):
#             print(x, cnt, idx)
#             if x > prices[idx]:
#                 print('111')
#                 ans.append((x,cnt, idx))
#             else:
#                 print("222")
#                 queue.append((x, cnt, idx))
                
#             if  idx < len(prices)-1:
#                 print("2.555", x, cnt, idx)
#                 queue.append((prices[idx+1],0,idx+1))

#             # else: # idx+1 = len(prices) - 1
#             #     ans.append((prices[idx], 0))
        
#         else: # idx == len(prices)-1
#             print("333", x, cnt, idx)
#             ans.append((x,cnt-1 ,idx))
#     print(ans)
#     return ans
                 
# prices=[1,2,3,2,3]

# def solution(prices):
#     answer = bfs(0, prices)
    
#     return answer
# solution(prices)

########################################################################



# def solution(prices):
#     answer = []
#     stack = []
#     stack2 = []
    
#     stack.append((0,prices[0]))
#     for i in range(1, len(prices)):
#         for j in range(len(stack)-1, -1, -1):
            
#                 if prices[i] < stack[j][1]:
#                     answer.append(i-j)
#                     stack.pop()
#                 else: # prices[i] >= stack[j][1]
#                     stack2.append(stack.pop())


#             # if prices[i] < stack[j][1]:
#             #     answer.append(i-stack[j][0])
#             #     stack.pop()
#             #     break
#             # else:
#             #     stack.append((i, prices[i]))
#     print(stack)
#     for k in range(len(stack)):
#         answer.append((len(prices)-stack[k][0]))
    

#     print(answer)
#     return answer

# prices = [1,2,3,2,3]
# solution(prices)



############################################################
# queue를 이용한 풀이

# from collections import deque

# def solution(prices):
#     answer = []
#     queue = deque(prices)
#     while queue:
#         price = queue.popleft()
#         sec = 1
#         flag = False
#         for i in queue:
#             if price <= i:
#                 sec += 1
#             else:
#                 answer.append(sec)
#                 flag = True
#                 break
#         if flag == False:
#             answer.append(sec-1)
#         flag = False
#         sec = 1


#     return answer

# prices = [1,2,3,2,3]
# print(solution(prices))


############################################################
# stack을 이용한 풀이

def solution(prices):
    answer = []
    stack = []

    for i in range(len(prices)):
        answer.append(len(prices)-i-1)
    print(answer)
    stack.append(0)
    
    for i in range(1, len(answer)):
        while stack and prices[stack[-1]] > prices[i]:
            x = stack.pop()
            answer[x] = i-x
        stack.append(i)
        print('stack',stack)

        
        
    return answer






prices = [1,2,3,2,3]
print(solution(prices))