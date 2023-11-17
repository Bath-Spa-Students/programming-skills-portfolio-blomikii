# Exercise 3: Your own list

'''Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”'''

###########################################################################################################

# Transportations in list
fave_transpo = ['car', 'airplane', 'bus', 'motor']

# Printing 
for item in fave_transpo:
    if item  == "car":
        print("I explore the city with my Mini Cooper.")
    elif item == "airplane":
        print("I travel to other countries with Singapore Airlines.")
    elif item == "bus":
        print("I go to other cities with Jam Liner.")
    elif item == "motor":
        print("I commute using my Vespa.")


