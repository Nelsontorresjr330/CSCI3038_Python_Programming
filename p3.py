import sys
from math import sqrt

def primes(start,end):

    if (end <= 1):
        yield False

    for x in range(start, end):

        prime_flag = 0

        if(x > 1):
            for i in range(2, int(sqrt(x))+1):
                if (x % i == 0):
                    prime_flag = 1
                    break
            if prime_flag == 0:
                yield x
            else:
                continue
        else:
            continue

for prime in primes(int(sys.argv[1]),int(sys.argv[2])):
    print(prime)