""" Simple logic we have to store every command value in a list then sum of our list is the final position of robots"""
for _ in range(int(input())):
    n = int(input())
    insturctions = []
    for i in range(n):
        m = input()
        ith =[int(i) for i in m.split() if i.isdigit()] # that will seperate ith-number from strings
        if m=='LEFT':
            insturctions.append(-1)
        elif m =='RIGHT':
            insturctions.append(1)
        else:
            if ith:
                insturctions.append(insturctions[ith[0]-1])
    print(sum(insturctions))
    
