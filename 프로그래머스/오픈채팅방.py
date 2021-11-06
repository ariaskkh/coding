def solution(record):
    answer = []
    for i in range(len(record)):
        answer.append(record[i].split())
        if answer[i][0] == 'Change':
            for j in range(i):
                if answer[j][1] == answer[i][1]:
                    answer[j][2] = answer[i][2]
            # del answer[i]
        elif answer[i][0] == 'Enter':
            q = 0
            while (q < i):
                if answer[q][0] != 'Leave' and answer[i][1] == answer[q][1]:
                    answer[q][2] = answer[i][2]
                q += 1
    key = []
    ans = []
    for k in range(len(answer)):
        if answer[k][0] == 'Enter':
            ans.append(answer[k][2] + "님이 들어왔습니다.")
            key.append((answer[k][1], answer[k][2]))
        elif answer[k][0] == 'Leave':
            for p in range(len(key)):
                if answer[k][1] == key[p][0]:
                    ans.append(key[p][1] + "님이 나갔습니다.")
    return ans

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))