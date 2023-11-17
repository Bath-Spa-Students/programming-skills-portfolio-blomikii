'''Write a Python program that uses a while loop to find the largest number among a series of  user-input values until they enter '0' to exit the loop.'''

###################################################################################################################

values = []

# Conditions
while True:
    value = int(input("Enter a series of numbers to find the largest number among them. Enter '0' to quit: "))
    
    if value != 0:
        values.append(value)
        print(f"{value} has been added to the series.")
    else:
        break

# Results
if values:
    max_value = max(values)
    print(f"The entered series of numbers: {values}")
    print(f"The largest number in the series is: {max_value}")
else:
    print("No numbers entered.")


