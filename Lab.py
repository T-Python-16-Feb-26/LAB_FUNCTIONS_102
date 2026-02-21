def find_primes(num1:int,num2:int):
    primes_number=[]
    for i in range(num1,num2+1):
        if i >1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:              
                primes_number.append(i)
    for i in primes_number:
        print(i)

user_input1=int(input("Enter the Start number: "))
user_input2=int(input("Enter the End number: "))
find_primes(user_input1,user_input2)