def find_primes(first: int, last: int):
    
    for num in range(first,last+1):
        

       # if num==1:
       #     print(num)
            
         if num > 1:
            
            for i in range(2, num):
                if (num % i) == 0:
                    
                    break
            else:
                
                print(num)


find_primes(25,50)
