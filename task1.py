def findPrime(num1: int, num2: int):
    for num in range(num1, num2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
findPrime(input1, input2)
    