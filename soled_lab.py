number_lower = int(input('Enter number lower : '))
number_upper = int (input('Enter number upper : '))
# To check the first number and second number and it must be as  following: first number is smaller than second number. 
while number_lower > number_upper:
    print('you should enter number upper > number lower ')
    number_lower = int(input('Please re-enter number lower : '))
    number_upper = int (input('Please re-enter number upper : '))

def find_primes ( first_number: int, second_numbre: int): 
    """
    this function to takes 2 parameters int     
    """
    for num in range(first_number , second_numbre + 1  ):
        if num > 1 :
            isPrime = True
            for i in range(2 , num):
                if num % i ==0:
                    isPrime = False
                    break
            if isPrime:
               print(num)

find_primes(number_lower, number_upper)
                 



