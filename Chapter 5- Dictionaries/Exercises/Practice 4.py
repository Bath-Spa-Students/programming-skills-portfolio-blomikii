'''Write a Python program to iterate through both the keys and values of a dictionary and print them '''

########################################################################################################

country_capitals = {"Azerbaijan": "Baku",
                    "South Korea": "Seoul",
                    "Afghanistan": "Kabul",
                    "Georgia": "Tblisi"}

for key, values in country_capitals.items():
    print(f"{key}: {values}\n")

    