from sys import stdin, stdout

next_array = [i for i in range(1, 100000+2)]
prev_array = [i for i in range(-1, 100000)]


while True:
    solder, report = list(map(int, stdin.readline().split()))
    
    if solder==report==0:
        break
    
    for i in range(1, solder+1):
        next_array[i] = i+1 
        prev_array[i] = i-1
    
    next_array[solder] = -1
    
    for j in range(report):
        left, right = list(map(int, stdin.readline().strip().split()))
        
        prv = prev_array[left]
        nex = next_array[right]
        if prv>0:
            next_array[prv] = next_array[right]
            
        if nex>0:
            prev_array[nex] = prev_array[left]
        
        stdout.write("{} {}\n".format(prev_array[left] if prv>0 else "*", next_array[right] if nex>0 else "*"))
        
    stdout.write("-\n")    
