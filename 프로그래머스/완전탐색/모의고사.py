from collections import deque

def solution(answers):
    answer = []
    tmp = []
    a1, a2, a3 = 0,0,0
    s1, s2, s3= deque(), deque(), deque()
    for i in range(1,6):
        s1.append(i)
    s2.append(2)
    s2.append(1)
    s2.append(2)
    s2.append(3)
    s2.append(2)
    s2.append(4)
    s2.append(2)
    s2.append(5)
    
    s3.append(3)
    s3.append(3)
    s3.append(1)
    s3.append(1)
    s3.append(2)
    s3.append(2)
    s3.append(4)
    s3.append(4)
    s3.append(5)
    s3.append(5)

    for j in answers:
        # print('j',j)
        if j == s1[0]:
            a1 += 1
        if j == s2[0]:
            a2 += 1
        if j == s3[0]:
            a3 += 1
        s1.rotate(-1)
        s2.rotate(-1)
        s3.rotate(-1)
    
    ## 두 번째 방법
    # tmp.append(a1)
    # tmp.append(a2)
    # tmp.append(a3)
    # max_s = max(tmp)
    # for i in range(3):
    #     if tmp[i] == max_s:
    #         answer.append(i+1)

    # 첫 번째 방법            
    tmp.append((a1,1))
    tmp.append((a2,2))
    tmp.append((a3,3))
    print(tmp)
    tmp1 = sorted(tmp, key=lambda x:(-x[0], x[1]))[:]
    print('tmp1',tmp1)
    
    for q in range(3):
        if tmp1[0][0] == tmp1[q][0]:
            answer.append(tmp1[q][1])
    print(answer)
    
    
    return answer