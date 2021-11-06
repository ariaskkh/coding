def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:

            arr.append((100 - progresses[i])//speeds[i]+1)
        else:
            arr.append((100 - progresses[i])//speeds[i])
    cnt = 1
    tmp = arr[0]
    for j in range(1, len(arr)):
        if tmp >=arr[j]:
            cnt +=1
        else: ## arr[j] > tmp
            answer.append(cnt)
            tmp = arr[j]
            cnt = 1
            print(answer, tmp, cnt,j, arr[j])
    if cnt != 0:
        answer.append(cnt)        
    return answer

# arr = [95, 90,99,99,80,99]
arr = [96,94]

# speeds = [1,1,1,1,1,1]
speeds = [3,3]
print(solution(arr, speeds))
