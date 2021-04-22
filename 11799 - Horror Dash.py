for t in range(int(input())):
    lst = list(map(int, input().split()))
    del lst[0]
    print('Case %d:'%(t+1),max(lst))
