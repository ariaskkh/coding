import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

tri = [list(map(int,input().split())) for _ in range(n)]
graph = [[0]*n for _ in range(n)]

def solution(tri):
    for i in range(1, len(tri)):
        for j in range(i+1):
            if j == 0:
                tri[i][j] += tri[i-1][j]
            elif j == i:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
    return max(tri[-1])
print(solution(tri))
                

