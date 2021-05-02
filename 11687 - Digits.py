while True:
    s = input()
    if s =='END':
        break
    elif s == '0':
        print('2')
    elif s == '1':
        print('1')
    else:
        l = len(s)
        s = str(l)
        cnt = 2
        while l!=1:
            l = len(s)
            s = str(l)
            cnt+=1
        
        print(cnt)
