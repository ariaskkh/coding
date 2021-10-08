import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []
prev = 0
flag = True
cnt = 0
for _ in range(n):
    strl = list(input().strip())
    
    for j in strl: 
        if j == prev: ## 전꺼랑 같을때
            if j not in arr:
                arr.append(j)
                prev = j
        else: ## 전꺼랑 다를 때. 새로운 문자
            if j not in arr:
                arr.append(j)
                prev = j
            else: ## 새로운 문자가 이미 arr에 존재 할 때
                flag = False
    if flag == True:
        cnt +=1
    flag = True
    arr = []
    prev = 0
print(cnt)