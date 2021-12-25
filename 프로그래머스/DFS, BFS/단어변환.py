from collections import deque

def check(x,y,n,words):
    cnt = 0
    for i in range(n):
        if words[x][i] != words[y][i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def bfs(tar,graph):
    queue = deque()
    ans = 0
    
    visited =  [0] * len(graph)
    visited[-1] = 1
    queue.append((graph[-1], ans, visited))
    while queue:
        a, ans1, visited1 = queue.popleft()
        
        for k in range(len(a)):
            if visited1[a[k]] == 0:
                visited1[a[k]] = 1
                queue.append((graph[a[k]], ans1+1, visited1))
                if a[k] == tar: # tart : idx
                    ans1+=1
                    return ans1
    

def solution(begin, target, words):
    answer = 0
    n = len(words[0])
    words.append(begin)
    
    if target not in words:
        print(0)
        return answer
        
    graph = [[] for _ in range(len(words))]
    for p in range(len(words)):
        for q in range(p, len(words)):
            if check(p,q,n,words) == True:
                graph[p].append(q)
                graph[q].append(p)
    
    targ = words.index(target)
    answer = bfs(targ, graph)
    
    return answer