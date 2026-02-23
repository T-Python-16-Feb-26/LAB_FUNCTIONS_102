
def find_primes (x, y):
    for n in range(x, y+1):
        if n > 1:
            prime = True

            for i in range( 2, n):
                if n % i ==0:
                    prime = False
                    break
                
            if prime:
                print(n)    
find_primes(25, 50)            