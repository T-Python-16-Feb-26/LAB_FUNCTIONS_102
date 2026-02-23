def find_primes(start: int, end: int):
    for num in range(start, end + 1):
        if num < 2:
            continue
         
        is_prime = True

        for div in range(2, num):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

find_primes(25, 50)

        

        
def split_camel_case(text):
    if type(text) != str:
        return "Error: input must be a string"

    result = ""

    for ch in text:
        if ch.isupper():
            result += " " + ch.lower()
        else:
            result += ch

    return result

print(split_camel_case("helloWorldThere"))
