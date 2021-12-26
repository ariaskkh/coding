## 10 분 컷

def solution(brown, yellow):
    answer = []
    tmp = []
    for prime_factor in range(1,round(yellow**0.5)+1):
        if yellow % prime_factor == 0: # 나눠 짐 !
            tmp.append((yellow//prime_factor,prime_factor))
    for i in tmp:
        if (i[0]+i[1])*2+4 == brown:
            answer = [i[0]+2, i[1]+2]
    return answer