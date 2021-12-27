from itertools import permutations

def prime_check(p, tmp1):
    for q in range(2,round(p**0.5)+1):
        if p % q != 0: # 소수임
            continue
        else: # 소수가 아님
            return False
    return True

def solution(numbers):
    answer = 0
    numbs = list(numbers)
    tmp = []
    tmp1 = []
    
    for i in range(1,len(numbs)+1):
        x = list(permutations(numbs, i))
        for j in x:
            print(int("".join(j)))
            if int("".join(j)) not in tmp1:
                tmp1.append(int("".join(j)))
            
    for p in tmp1:
        if p == 0 or p == 1:
            continue
        if prime_check(p, tmp1) == True:
            answer+=1
    
    return answer