'''Write a Python program that uses a function to check if a given number is prime or not.'''

#######################################################################################

# Function
def is_prime(number):
    if number<2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True

# Checking
num = 15
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number.")

    