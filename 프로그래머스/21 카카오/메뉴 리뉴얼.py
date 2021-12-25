####################################

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        candidate = []
        for order in orders:
            for combi in combinations(order,i):
                candidate.append("".join(sorted(combi)))
        c_candi = Counter(candidate)
        
        for j in c_candi:
            if c_candi[j] > 1 and c_candi[j] == max(c_candi.values()):
                answer.append(j)
        
    return sorted(answer)