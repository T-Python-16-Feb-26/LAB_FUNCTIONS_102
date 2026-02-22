def find_prime_numbers(start_number: int, end_number: int) -> list:
    """
    Return a list of prime numbers between two numbers .

    Args:
        start_number (int): The first number in the search range.
        end_number (int): The last number in the search range.

    Returns:
        list[int]: A list of prime numbers between the given range.
    """

    prime_numbers_list = []

    for current_number in range(start_number, end_number + 1):

        if current_number < 2:
            continue

        is_prime = True

        for divisor in range(2, current_number):
            if current_number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers_list.append(current_number)

    return prime_numbers_list


# User Input 
print("Enter the range to search for prime numbers between them.")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print("\nPrime numbers in this range:")

result = find_prime_numbers(first_number, second_number)

# Print each element in the list line by line
for number in result:
    print(number)
