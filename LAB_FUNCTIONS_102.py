def find_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:  # primes are greater than 1
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)
find_primes(2, 10)



    
