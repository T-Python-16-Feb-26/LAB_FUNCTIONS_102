import math


def find_primes(first_number:int , second_number:int):
    if first_number == 1:
        first_number = 2
    for i in range(first_number,second_number+1,1):
        sqare_number = math.sqrt(i)
        is_prime = True
        for j in range(2,int(sqare_number)+1,1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            print(i)
                




first_number = int(input("write the first number: "))
second_number = int(input("write the second number: "))

find_primes(first_number,second_number)