def find_primes(number1: int, number2: int):
    for n in range(number1, number2 + 1):
        if n < 2:
            continue
        is_prime = True
        for n2 in range(2, int(n ** 0.5) + 1):
            if n % n2 == 0:
                is_prime = False
                break
        if is_prime:
            print(n)

find_primes(25, 50)