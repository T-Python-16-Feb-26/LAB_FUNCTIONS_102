def find_primes(start: int, end: int):
    for number in range(start, end + 1):
        if number < 2:
            continue
        
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0: # if divisible by any number other than 1 and itself, it's not prime
                is_prime = False
                break
        
        if is_prime:
            print(number)

find_primes(25, 50)