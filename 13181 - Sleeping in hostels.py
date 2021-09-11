try:
    while True:
        s = input()
        ret = 0
        prev = -1
        n = len(s)
        for i in range(n):
            if s[i] == 'X':
                if prev == -1:
                    ret = max(ret, i-1)
                    prev = i 
                else:
                    ret = max(ret, (i-prev-2)//2)
                    prev = i 
        if prev != n-1:
            ret = max(ret, n-prev-2)
            
        print(ret)


except:
    pass
