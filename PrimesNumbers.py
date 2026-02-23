def find_primes(num1, num2):
    for number in range(num1, num2 + 1):
        if number < 2:
            continue
        
        is_prime = True
        divisor = 2
        
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        
        if is_prime:
            print(number)
            
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

find_primes(num1, num2)