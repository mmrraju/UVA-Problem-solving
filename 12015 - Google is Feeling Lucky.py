for t in range(int(input())):
    d = dict()
    for i in range(10):
        url, space, rank = input().rpartition(' ')
        d[url] = int(rank)
        
    max_val = max(d.values())    
    print('Case #%d:'%(t+1))
    for url, rank in d.items():
       if  rank == max_val:
           print(url)
