# Problem 1: Reverse string
def string_reverser(input_str: str):
    #Reverse string using splicing syntax with "[::-1]" so it reads and prints backwards
    reversed_string = input_str[::-1]
    return reversed_string

# Optional Function test
# input_str = input('Enter String: ')
# reversed_str = string_reverser(input_str)
# print('Input: ', input_str)
# print('Reversed:', reversed_str)


# Problem 2: Palindrome Check

def palindrome_checker(input_str: str):
    # Convert the input string to lowercase and remove spaces so it would ignore Uppercase and also spaces in a sentence
    input_str = input_str.lower().replace(' ', '')
    # Check if the string is equal to its reverse with "[::-1]"
    is_palindrome = input_str == input_str[::-1]
    return is_palindrome

# Optional Function test
# input_str = input('Enter String: ')
# is_palindrome = palindrome_checker(input_str)
# print('Input:', input_str)
# print('Is Palindrome:', is_palindrome)


# Problem 3: Prime Number Generator

def prime_number_generator(limit: int):
    prime_list = []
    # use "limit + 1" to include the ending value of limit
    for i in range(2, limit + 1):
        #set default is_prime to True and only change to False when it has factors other than itself 
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list

# Optional Test the function
# limit = int(input('Enter limit: '))
# prime_list = prime_number_generator(limit)
# print(f"Prime numbers up to {limit}: {prime_list}")





