#lab function 102

def find_primes(x:int, y:int):
    '''This function will find all the prime numbers between x and y'''
    for number in range(x, y+1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)
find_primes(25, 50)