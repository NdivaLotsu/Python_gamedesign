def is_even(number):
    """Check if the given number is even."""
    return number % 2 == 0

def is_odd(number):
    """Check if the given number is odd."""
    return number % 2 != 0

# Example usage:
#user_input = int(input("Enter a number: "))

#if is_even(user_input):
    #print(f"{user_input} is an even number.")
#else:
    #print(f"{user_input} is an odd number.")





def is_even(number):
    if number % 2 != 0:
        return True 
    else:
        return None
    
def is_prime (number):
    if number % 2 != 0:
        return True
    else:
        return None
    
def check_prime_or_even(number,primeFunc,evenFunc):
    if number < 2:
        print("not prime nor even")
    else:
        if primeFunc(number) != None:
            print(primeFunc(number),"This is a prime number")
        elif evenFunc(number) != None:
            print(primeFunc(number),"This is a prime number")


check_prime_or_even(10,is_prime,is_even)
