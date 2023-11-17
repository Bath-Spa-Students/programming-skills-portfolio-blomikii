# Exercise 2: Movie Tickets

'''A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket'''

###############################################################################################################

print("Welcome to the Cinema")

prompt = "What is your age?"

# Checking age 
while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("Your ticket is free!")
    elif age < 13:
        print("Your ticket costs $10")
    else:
        print("Youre ticket is $15")
    
