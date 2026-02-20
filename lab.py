def is_primes(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5), +1):
        if n%i == 0:
            return False
    return True

def find_primes(a, b):
    start = min(a, b)
    end = max(a,b)

    for num in range (start, end +1):
        if is_primes (num):
            print(num)

find_primes(25, 50)
