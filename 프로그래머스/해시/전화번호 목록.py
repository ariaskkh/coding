# #### 그냥 품. 시간 초과 2개

# def check(x,y):
    
#     if len(x) < len(y):
#         if x == y[:len(x)]:
#             return False
#     else:
#         if x[:len(y)] == y:
#             return False
#     return True

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             answer = check(phone_book[i], phone_book[j])
#             if answer == False:
#                 return answer
    
#     return answer

########################################################################
# 위 풀이 최적화 통과
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:(len(phone_book[i]))] == phone_book[i]:
                answer = False
                return answer
    
    return answer
###############################################################
## 해시

