from heapq import heappop, heappush

def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []
    
    while i < len(jobs): # i는 일을 처리했을 때 올라감
        for job in jobs:
            if start <job[0] <= now:
                heappush(heap, (job[1],job[0])) # 소요시간, 요청 시점
        if len(heap) >0:
            current = heappop(heap)
            current[0]
            start = now # 바로 이전에 완료한 작업의 시작 시간
            now += current[0]
            answer += now - current[1]
            i += 1            
        else:
            now +=1
                
    return int(answer//len(jobs))


################################################################
# 더 직관적인 풀이

def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x:x[1])
    
    while len(jobs):
        for i in range(len(jobs)): # 요청 시간, 소요 시간
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                jobs.pop(i)
                # jobs.remove(jobs[i])
                break
            if i == len(jobs)-1:
                time += 1
                
    return answer//n