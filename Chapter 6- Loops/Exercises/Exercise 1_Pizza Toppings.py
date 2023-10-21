## Exercise 1: Pizza Toppings 

''' Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza. '''

###############################################################################################################

toppings = []

while True:
    topping = input("What toppings would you like on your pizza? To finish, enter 'quit': ")
    if topping != 'quit':
        toppings.append(topping)
        print(f"{topping} has been added to your pizza.")
    else:
        break

print("Your pizza is ready with the followings: ")
for topping in toppings:
    print(topping)
