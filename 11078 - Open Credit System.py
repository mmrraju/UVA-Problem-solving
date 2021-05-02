for t in range(int(input())):
    lst = []
    n = int(input())
    for i in range(n):
        s = int(input())
        lst.append(s)
    final_max = lst[0] - lst[1]
    cur_max = lst[0]
    for m in range(1, n):
        if (final_max < cur_max - lst[m]):
            final_max = cur_max - lst[m]
            
        if cur_max < lst[m]:
            cur_max = lst[m]
            
    print(final_max)
        
