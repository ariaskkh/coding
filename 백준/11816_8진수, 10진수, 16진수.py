x = input()

if x[0] == '0':
    if x[1] == 'x': # 16진수 
        num = x[2:]
        print(int(num,16))
    else: # 8 진수
        num = x[1:]
        print(int(num, 8))
else:
    print(int(x))