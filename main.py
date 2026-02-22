def find_primes(start ,end):
    print(f"primes between {start} and {end} are:")
    for num in range(start,end+1):

        if num >1:
            for i in range(2,int(num//2)+1):
                if (num % i) ==0:
                    break
            else:
              print(num)
find_primes(33,73)