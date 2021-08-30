import sys
input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    M = int(input().strip())
    t = []
    for _ in range(M):
        x,y  = map(int, input().split())
        t.append((x,y))
    # 오름차순 정렬
    t.sort()
    cnt = 0
    # 서류 1등은 합격이므로 +1
    people =1
    mmin = t[0][1]
    # 서류 오름 차순에서 i 번째 면접 점수는 1 ~ i-1 번째의 면접 등수보다 높아야한다(1에 가까워야) 즉 1~ i-1의 최소값 보다 낮으면 됨
    for i in range(1,len(t)):
        if mmin >= t[i][1]:
            people += 1
            mmin = t[i][1]
    print(people)