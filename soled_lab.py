number_lower = int(input('Enter number lower : '))
number_upper = int (input('Enter number upper : '))
while number_lower > number_upper:
    print('you should enter number upper > number lower ')
    number_lower = int(input('Please re-enter number lower : '))
    number_upper = int (input('Please re-enter number upper : '))

def find_primes ( first_number: int, second_numbre: int):
    for num in range(first_number , second_numbre + 1  ):
        if num > 1 :
            pri = True
            for i in range(2 , num):
                if num % i ==0:
                    pri = False
                    break
            if pri:
               print(num)

find_primes(20, 40)
                 



