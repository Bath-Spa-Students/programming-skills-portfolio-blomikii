#Exercise 5: Pets

'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet'''

############################################################################################################

pets = [
    {
        "animal" : "Cat",
        "pet name" : "Kyo",
        "owner" : "Samantha"
    },
    {
        "animal" : "Dog",
        "pet name" : "Chuchu",
        "owner" : "Harvey"
    },
    {
        "animal" : "Fish",
        "pet name" : "Goldielyn",
        "owner" : "Linus"
    },
]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Pet Name: {pet['pet name']}")
    print(f"Owner: {pet['owner']}")
    print()

