#Exercise 4

rivers = {
    "Mississippi": "United States of America",
    "Yenisei": "Russia and Mongolia",
    "Nile": "Egypt",
    "Amazon": "Peru, Brazil, and Colombia",
    "Huang He": "China",
}

for river, country in rivers.items():
    print(f"The {river} river flows through {country}.\n")

print("\nThe following are the rivers listed in the dictionary:")
for river in rivers.keys():
    print(f"• {river}")

print("\nThe following are the countries listed in the dictionary:")
for country in rivers.values():
    print(f"• {country}")



