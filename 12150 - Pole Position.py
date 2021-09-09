while True:
    n = int(input())
    if n==0:
        break
    
    err = 0
    lst = [0]*10**4
    for i in range(n):
        car_number, position = list(map(int, input().split()))
        
        if i+position<0:
            err = 1 
            
        if i+position>=n:
            err = 1 
            
        if err==0 and lst[i+position]:
            err = 1 
            
        if err:
            continue
        
        lst[i+position] = car_number
    if err:
        print("-1")
        continue
    
    print(*lst[:n])
        
