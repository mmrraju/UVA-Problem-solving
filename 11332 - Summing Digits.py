while True:
    n = int(input())
    digit_sum = 0
    if n == 0:
        break
    while (n > 0 or digit_sum > 9):
        if n == 0:
            n = digit_sum
            digit_sum = 0 
        reminder = n % 10
        digit_sum = digit_sum + reminder
        n = n // 10
    print(digit_sum)
        
