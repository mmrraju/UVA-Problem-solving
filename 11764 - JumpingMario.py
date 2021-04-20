for t in range(int(input())):
    walls = int(input())
    wall_list = list(map(int, input().split()))
    high_jump = 0
    low_jump = 0
    l = len(wall_list)
    for i in range(l):
        if i == l-1:
            break
        if wall_list[i]==wall_list[i+1]:
            continue
        if (wall_list[i]<wall_list[i+1]):
            high_jump +=1 
        else:
            low_jump +=1
        
    print('Case %d:'%(t+1),'%d'%high_jump, '%d'%low_jump)
        
