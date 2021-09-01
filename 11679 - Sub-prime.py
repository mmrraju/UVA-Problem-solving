while (True):
    Bank, N  = map(int, input().split())
    if Bank == 0 and N==0:
        break
    Monetary_reserve = [int(x) for x in input().split()]
    
        
    for i in range(0, N):
        debit, credit, v = map(int, input().split())
        Monetary_reserve[credit-1] += v
        Monetary_reserve[debit-1] -= v
            
    
    flag = True        
    for i in range(Bank):
        if Monetary_reserve[i]<0:
            flag = False
            break
    
    if flag:
        print("S")
    else:
        print("N")
    
    
