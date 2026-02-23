
def find_prime(start,end):
    '''
    this takes 2 numbers,
    check if they are 1 or less then 1 to exclude the nigative numbers, 
    then finds the prime numbers between them and prints them

    args:
      start (int): the number to start from
      end (int): the number to end at

    returns:
      prints the prime numbers between start and end

    '''
    for n in range(start,end+1):
      if n <= 1:
        continue
      else:
        for lesser_then_root in range(2,int(n**0.5)+1):
            if n % lesser_then_root == 0:
               break
        else:
            print(n)
            
find_prime(25,50)
    