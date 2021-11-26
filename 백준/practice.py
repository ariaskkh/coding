import sys
input = sys.stdin.readline

def dfs(i):
    visited[i] = 1
    for k in graph[i]:
        if not visited[k]:
            dfs(k)

n = int(input().strip())
kinds = int(input().strip())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(1,kinds+1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
print(visited)
# j = 1

# while visited[j] != 0:
#     for k in range(len(graph[j])):
#         j = graph[k]
#     visited[j] = 1

    # print(j, graph[j])
# print(visited)

dfs(1)
print(sum(visited)-1)