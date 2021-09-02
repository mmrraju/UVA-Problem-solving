""" Solved by MMR Raju """
try:
    while(True):
        participates, budget, hotels, weeks = map(int, input().split())
        dn = False
        m = budget
        for _ in range(hotels):
            perhead_cost = int(input())
            week = list(map(int, input().split()))
            for i in range(weeks):
                if perhead_cost*participates<=budget and week[i]>=participates:
                    if perhead_cost*participates<=m:
                        dn = True
                        m = perhead_cost*participates
                    
        if dn:
            print(m)
        else:
            print('stay home')
                    

except:
    pass
