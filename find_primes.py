def find_primes(p1, p2):


    for num in range(p1, p2 + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

find_primes()

