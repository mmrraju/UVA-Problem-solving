t = 0
def EmoodleBalance(n):
    global t 
    lst = list(map(int, input().split()))
    l = len(lst)
    y_treat= 0
    n_treat = 0
    t +=1 
    for i in range(l):
        if lst[i] ==0:
            y_treat +=1 
        else:
            n_treat +=1 
    print("Case %d:"%t, (n_treat-y_treat) )
    
while True:
    n = int(input())
    if n==0:
        break
    else:
        EmoodleBalance(n)
