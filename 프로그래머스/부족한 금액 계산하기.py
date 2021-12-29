def n_sum(n):
    cnt = 0
    for i in range(1,n+1):
        cnt += i
    return cnt

def solution(price, money, count):
    answer = -1
    answer = price*n_sum(count) - money
    
    return answer if answer >=0 else 0