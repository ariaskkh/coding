import sys
input = sys.stdin.readline

N = int(input().strip())
time = []
for _  in range(N):
    x, y = map(int, input().split())
    time.append((x,y))

time.sort() # 시작 시간 오름차순 정렬

min_time = time[0][1] # 처음 시작 회의의 끝나는 시간을 min_time으로 받기
cnt = 0
for i in range(1,len(time)): # 1, ~ list_time 시간까지
    if time[i][0] < min_time:
        if min_time > time[i][1]:
            min_time = time[i][1] 
    else: # i 가 min_time 이상일 떄
        cnt +=1
        min_time = time[i][1] # min_time을 다시 갱신하기
    
print(cnt+1)

########################################################################
## 서자헌 형 풀이