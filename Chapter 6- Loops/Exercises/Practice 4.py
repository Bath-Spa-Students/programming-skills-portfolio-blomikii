'''Write a Python program that uses the break statement to exit a for loop when a specific condition is met.'''

##############################################################################################################

sum_numbers = 0

for i in range(1, 101):
    sum_numbers += i
    
    if sum_numbers > 200:
        print(f"Breaking the loop because the sum exceeds 200. Current sum: {sum_numbers}")
        break

print(f"The sum of numbers from 1 to 100 or until the sum exceeds 200: {sum_numbers}")

