''' Here given an array, we have to calculate absulate difference of elemnts. Then store a new array and need to sort it. then check array elements is 1 to (n-1)
range.'''
try:
    while(True):
        lst = [int(i) for i in input().split()]
        n = lst[0]
        lst = lst[1:]
        result = []
        flag = True
        for i in range(1, n):
            result.append(abs(lst[i] - lst[i-1]))
            
        result.sort()
        for i in range(n-1):
            if result[i] != i+1:
                flag = False
        
        if flag==False:
            print("Not jolly")
        else:
            print("Jolly")
except:       
    pass
