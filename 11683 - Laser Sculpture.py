""" Linear scan. Traverse the list. If is the first time save the diference between the row and current list position(set current equal to list current position), 
otherwise if the current list position  is less than current variable save the diference between current and the current list position. """
while True:
    row, column = map(int, input().split())
    if row==column==0:
        break
    final_length = list(map(int, input().split()))
    total = 0
    
    for i in range(column):
        if i == 0:
            total = row - final_length[i]
            current = final_length[i]
        else:
            if final_length[i]<current:
                total = total + (current - final_length[i])
        
        current = final_length[i]
    
    print(total)
