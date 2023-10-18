#Exercise 4: Rivers

'''Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary.'''

#############################################################################################################

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



