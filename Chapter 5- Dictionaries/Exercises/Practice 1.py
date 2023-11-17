'''Use a dictionary to store information about yourself'''

############################################################

myself = {
    "Name": "Samantha Mendoza",
    "Birthday": "October 25",
    "Age": 18,
    "Nationality": "Filipino"
}

for info, me in myself.items():
    print(f"{info}: \n{me}\n")

    