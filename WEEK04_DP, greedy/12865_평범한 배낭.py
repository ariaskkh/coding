## 처음 코드

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(1, K+1):
        if i == 1:
            if w <= j:
                bag[i][j] = v
            else:
                bag[i][j] = 0
        else:
            if w <= j:
                if bag[i-1][j] == 0 :
                    bag[i][j] = v
                # 새 물건을 넣고 난 나머지 무게에 대한 가치 : bag[i-1][j-w]
                else:
                    bag[i][j] = max(bag[i-1][j], v + bag[i-1][j-w])
            else:
                bag[i][j] = bag[i-1][j]
print(bag[N][K])

##################################################################
import sys
input = sys.stdin.readline
# N 물건 개수, K 최대 무게 받음
N, K = map(int, input().split())
# dp table 을 만듦. 이때 x축은 물건 개수 및 종류, y축은 무게 weight, 값은 최대 value
# dp_bag[i][j] 는 i 개의 물건을 최대무게 j로 할 때의 최대 value
dp_bag = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = map(int, input().split()) # 물건의 무게 및 value
    for j in range(1, K+1):
        if j < w: # j: 최대 무게, w: 물건 무게. 가방 최대 무게가 물건 무게보다 작을 떄
            dp_bag[i][j] = dp_bag[i-1][j]
        else: # 가방 최대 무게가 물건 무게보다 클 때
            dp_bag[i][j] = max(dp_bag[i-1][j], v + dp_bag[i-1][j-w]) # j-w: i 번 째 물건을 넣고 난 후 남은 가방의 여유 무게
print(dp_bag[N][K])

##################################################################
## 수정 코드

n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])