#Exercise 5

pets = [
    {
        "animal" : "cat",
        "pet name" : "kyo",
        "owner" : "sammie"
    },
    {
        "animal" : "dog",
        "pet name" : "chuchu",
        "owner" : "mc"
    },
    {
        "animal" : "fish",
        "pet name" : "glodielyn",
        "owner" : "jhun"
    },
]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Pet Name: {pet['pet name']}")
    print(f"Owner: {pet['owner']}")
    print()

