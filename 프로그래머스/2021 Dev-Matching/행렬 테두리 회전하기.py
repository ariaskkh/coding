# def c_rotation(rows, columns,query, table, answer):
#     x1,y1,x2,y2 = query[0],query[1],query[2],query[3]
#     tmp = 0
    
#     tmp_t = table[x1-1][y2-1]
#     tmp_b = table[x2-1][y1-1]
#     tmp_l = table[x1][y1-1]
#     tmp_r = table[x2-2][y2-1]
#     min_v = min(tmp_t, tmp_b, tmp_l, tmp_r)
#     # 위
#     for q1 in range(y2-2, y1-2,-1):
#         table[x1-1][q1+1] = table[x1-1][q1]
#         min_v = min(min_v, table[x1-1][q1+1])
#     table[x1-1][y1-1] = tmp_l
    
#     # 아래
#     for q2 in range(y1-1, y2-1):
#         table[x2-1][q2] = table[x2-1][q2+1]
#         min_v = min(min_v, table[x2-1][q2])
    
#     # 왼
#     for q3 in range(x1-1, x2-2):
#         table[q3][y1-1] = table[q3+1][y1-1]
#         min_v = min(min_v, table[q3][y1-1])
#     table[x2-2][y1-1] = tmp_b
    
#     # 오
#     for q4 in range(x2-1, x1, -1):
#         table[q4][y2-1] = table[q4-1][y2-1]
#         min_v = min(min_v, table[q4][y2-1])
#     table[x1][y2-1] = tmp_t
#     answer.append(min_v)

# def solution(rows, columns, queries):
#     answer = []
#     t = []
#     table = []
    
#     for j in range(0, rows):
#         for i in range(1,columns+1):
#             t.append(i+j*columns)
#         table.append(t)
#         t=[]
#     # print(table)
#     for query in queries:
#         c_rotation(rows, columns, query, table, answer)
    
#     return answer

############################################################
## rotate를 이용한 풀이... 미쳤다 진짜

from collections import deque
def solution(rows, columns, queries):
    answer = []
    edges = deque()
    arr = [[i+columns*j for i in range(1, columns+1)] for j in range(rows)]
    
    
    for query in queries:
        x1,y1,x2,y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        # queue에 넣기, 최솟값 구하기, 회전
        # 상
        for q1 in range(y2-y1):
            edges.append(arr[x1][y1+q1])
        # 우
        for q2 in range(x2-x1):
            edges.append(arr[x1+q2][y2])
        # 하
        for q3 in range(y2-y1):
            edges.append(arr[x2][y2-q3])
        # 좌
        for q4 in range(x2-x1):
            edges.append(arr[x2-q4][y1])
        
        answer.append(min(edges)) # 최솟값
        edges.rotate(1) # 회전
        
        # 행렬 변경
        # 상
        for q1 in range(y2-y1):
            # edges.append(arr[x1][y1+q1])
            arr[x1][y1+q1] = edges.popleft()
        # 우
        for q2 in range(x2-x1):
            # edges.append(arr[x1+q2][y2])
            arr[x1+q2][y2] = edges.popleft()
        # 하
        for q3 in range(y2-y1):
            # edges.append(arr[x2][y2-q3])
            arr[x2][y2-q3] = edges.popleft()
        # 좌
        for q4 in range(x2-x1):
            # edges.append(arr[x2-q4][y1])
            arr[x2-q4][y1] = edges.popleft()
    return answer