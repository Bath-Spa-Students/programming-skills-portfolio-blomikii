#Exercise 5

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

