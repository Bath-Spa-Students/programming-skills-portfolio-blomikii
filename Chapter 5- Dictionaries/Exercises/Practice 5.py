'''Write a Python program to merge two dictionaries into one.'''

################################################################

country_capitals1 = {"Japan": "Tokyo",
                    "South Korea": "Seoul"}

country_capitals2= {"Armenia": "Yerevan",
                    "Bahrain": "Manama"}

merged = {**country_capitals1, **country_capitals2}

for key, values in merged.items():
    print(f"{key}: {values}\n")

    