"""
# LAB_FUNCTIONS_102

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between `25` and `50` are:

29   
31   
37   
41   
43   
47   
"""
def find_prime(start:int, end:int):
    """This function takes two integers and find the prime numbers between them, and return a list of them"""

    primes = []
    for i in range(2, end+1): # we find all primes until the end parameter
        is_prime = True # we assume all is prime until its not
        for j in primes: # we loop throgh the primes we have
            if i%j == 0: # exclude any that can be divided by primes we have
                is_prime = False
                break
        if is_prime: # if it cannot be divided by primes we add it
            primes.append(i)
    # filter all primes to get the peimes between start and end parameters
    primes_between = []
    for i in primes:
        if start <= i:
            primes_between.append(i)
    return primes_between



print(find_prime(0, 2)) # [2]

print(find_prime(2, 3)) # [2, 3]

print(find_prime(25, 50)) # [29, 31, 37, 41, 43, 47]

print(find_prime(3, 10)) # [3, 5, 7]

print(find_prime(14000, 15000))
"""
    [14009, 14011, 14029, 14033, 14051, 14057, 14071, 14081, 14083, 14087, 14107, 
    14143, 14149, 14153, 14159, 14173, 14177, 14197, 14207, 14221, 14243, 14249, 
    14251, 14281, 14293, 14303, 14321, 14323, 14327, 14341, 14347, 14369, 14387, 
    14389, 14401, 14407, 14411, 14419, 14423, 14431, 14437, 14447, 14449, 14461, 
    14479, 14489, 14503, 14519, 14533, 14537, 14543, 14549, 14551, 14557, 14561, 
    14563, 14591, 14593, 14621, 14627, 14629, 14633, 14639, 14653, 14657, 14669, 
    14683, 14699, 14713, 14717, 14723, 14731, 14737, 14741, 14747, 14753, 14759, 
    14767, 14771, 14779, 14783, 14797, 14813, 14821, 14827, 14831, 14843, 14851, 
    14867, 14869, 14879, 14887, 14891, 14897, 14923, 14929, 14939, 14947, 14951, 
    14957, 14969, 14983]
"""