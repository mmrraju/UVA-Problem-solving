from itertools import combinations
n = int(input())
l = input().split()
k = int(input())

C = list(combinations(l, k))
f = filter(lambda x: 'a' in x, C )
print("{0:.3}".format(len(list(f))/len(C)))
            
