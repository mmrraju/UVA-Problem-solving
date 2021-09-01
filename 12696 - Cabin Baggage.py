p = 0
for _ in range(int(input())):
    lst = list(map(float, input().split()))
    volume = sum(lst[:3])
    weight = lst[-1]
    if volume<=125 and weight<=7:
        p +=1
        print(1)
    elif lst[0]==56 and lst[1]==45 and lst[2]==25 and weight<=7.00:
        p +=1
        print(1)
    else:
        print(0)
print(p)
