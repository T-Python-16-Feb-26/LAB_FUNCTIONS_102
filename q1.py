def find_primes(num1:int, num2:int):    
   for x in range(num1, num2 + 1):
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    break  
            else:
                print(x)
find_primes(25, 50)

