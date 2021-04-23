from functools import reduce

sum_digit = lambda num: (num)%10 + (num)//10
count_ch = lambda ch: sum_digit(ord(ch) - ord('A') + 1 ) if ch.isupper() else sum_digit(ord(ch)-ord('a')+1 ) if ch.islower() else 0 

while True:
    try:
        a = input()
        b = input()
        sum_a = reduce((lambda x, y: sum_digit(x+y)), map(count_ch, a))
        sum_b = reduce((lambda x, y: sum_digit(x+y)), map(count_ch, b))
        
        if sum_a<sum_b:
            ratio = sum_a/sum_b
        else:
            ratio = sum_b/sum_a
        
        print("{:.2f} %".format(ratio*100))
    except EOFError:
        break
