def solution(n, k, cmd):
    answer = ''
    
    linked_list = {i: [i-1,i+1] for i in range(1, n+1)}
    print(linked_list)
    OX = ["O"] * (n+1)
    stack = []
    
    k += 1 # idx를 하나 올려줌
    
    for c in cmd:
        if c[0] == "U":
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == "D":
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == "C":
            prev, next = linked_list[k]
            stack.append([prev,next,k])
            OX[k] = "X"
            
            # 제일 마지막 여부 k 처리
            if next == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]
            # 제거 후 앞 뒤로 연결
            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else: 
                linked_list[prev][1] = next
                linked_list[next][0] = prev
                
        elif c[0] == "Z":
            prev, next, now = stack.pop()
            OX[now] = 'O'
            
            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now
    # print(OX)
    return "".join(OX[1:])

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
solution(n,k,cmd)