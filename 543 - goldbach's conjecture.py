import bisect

def SievOf(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2*i + 1 
            tmp = ((size-1) - i) //val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def index(a, x, start):
    i = bisect.bisect_left(a, x, start)
    if i != len(a) and a[i] == x:
        return i 
    return None
primes = SievOf(1000001)
while True:
    n = int(input())
    if n == 0:
        break
    for i, prime in enumerate(primes):
        if prime*2>n :
            break
        loc = index(primes, n-prime, i)
        if loc:
            print("{} = {} + {}".format(n, prime, primes[loc]))
            break
