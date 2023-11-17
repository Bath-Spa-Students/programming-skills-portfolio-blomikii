'''Write a Python function that calculates the factorial of a given positive integer using recursion.'''

######################################################################################################

# Function
def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)
    
# Testing
input = int(input("Enter a positive integer: "))
output = factorial(input)

# Result
print(f"The factorial of {input} is {output}")


