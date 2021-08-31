# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# time = []
# for _  in range(N):
#     x, y = map(int, input().split())
#     time.append((x,y))

# time.sort() # 시작 시간 오름차순 정렬

# min_time = time[0][1] # 처음 시작 회의의 끝나는 시간을 min_time으로 받기
# cnt = 0
# for i in range(1,len(time)): # 1, ~ list_time 시간까지
#     if time[i][0] < min_time:
#         if min_time > time[i][1]:
#             min_time = time[i][1] 
#     else: # i 가 min_time 이상일 떄
#         cnt +=1
#         min_time = time[i][1] # min_time을 다시 갱신하기
    
# print(cnt+1)

########################################################################
## 서자헌 형 풀이

import sys

N = int(sys.stdin.readline())
teams = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 1단계: 종료 시간 순으로 정렬(오름차순)
# - 종료 시간이 동일한 경우, 시작 시간 순으로 정렬
teams.sort(key=lambda t: (t[1], t[0]))

# 2단계: 기준에 맞게 하나씩 선택
# - 1) 종료 시간이 가장 빠른 팀 선택
# - 2) 선택된 팀과 양립 불가능한 팀 제거
# - 3) 남은 팀이 있을 때까지 1,2 절차 반복

selected = []
i = -1
last_finish_time = 0
while i < len(teams)-1:
    i += 1
    team = teams[i]
    ts, tf = team
    # 남은 팀들 중 시작 시간이 선택된 마지막 팀의 종료 시간보다 빠른 팀 제외
    if ts < last_finish_time:
        continue 
    # 종료 시간이 가장 빠른 팀을 선택
    # (종료 시간 순으로 정렬되어 있으므로 가장 앞에 있는 팀)
    last_finish_time = tf
    selected.append(team)

print(selected)
print(len(selected))