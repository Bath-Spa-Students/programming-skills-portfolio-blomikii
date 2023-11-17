# Exercise 5: No Pastrami

''' Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches. '''

##############################################################################################################

# List of sandwhich orders
sandwich_orders = [
    'tuna',
    'pastrami',
    'grilled cheese',
    'chicken and mushroom',
    'pastrami',
    'salami',
    'pastrami',
]

# Empty list for finished sandwhiches
finished_sandwiches = []

# Removing pastrami from the list
print("Sorry, we're out of pastrami today.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print()

# Making sandwhiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am currently making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Finished sandwhiches
print()
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} sandwich is ready!")

