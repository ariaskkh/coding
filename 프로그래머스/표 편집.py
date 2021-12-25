def solution(n, k, cmd):
    # print('k:', k)
    answer = ''
    visited = [0] * (n)
    dict = {}
    stack = []
    for z in range(n):
        dict[z] = 1
    # print(dict)
    # print('k:', k)
    # dict.pop(1)
    # print(dict, k)
    
    for x in cmd:
        if len(x) == 1:
            
            if x == "C": # 제거인 경우
                print(111)
                print('k:',k)
                print('dict',dict)
                # dict.pop(1)
                # print(dict)
                y = dict.pop(k)
                # print(y)
                stack.append((k,y)) # 딕셔너리에서 k번째를 뺴주고 그 값을 stack에 넣음
            else: # x == "Z", 되돌릴 경우
                print(222)
                k1, y1 = stack.pop()
                dict[k1] = 1 # stack에서 나온 값을 dict에 넣어주며 value는 0으로 다르게
        else:
            if x[0] == "U":
                print(333)
                k -= int(x[2])
            else: # x[0] == "D"
                print(444)
                k += int(x[2])
    print('hihi',dict)
    
    for m in range(n):
        if m in dict.keys():
            answer += 'O'
        else:
            answer += 'X'
    print(answer)
    return answer

n = 8
k =2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
solution(n,k,cmd)