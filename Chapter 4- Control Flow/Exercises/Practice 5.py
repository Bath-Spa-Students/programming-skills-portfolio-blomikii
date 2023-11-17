'''Write a Python program that uses the elif statement to determine the season based on the 
month provided as input'''

####################################################################################################

month = input("Enter a month (e.g., January): ").lower()

# Conditions
if month in {'december', 'january', 'february'}:
    season = 'Winter'
elif month in {'march', 'april', 'may'}:
    season = 'Spring'
elif month in {'june', 'july', 'august'}:
    season = 'Summer'
elif month in {'september', 'october', 'november'}:
    season = 'Autumn'
else:
    season = 'Invalid Input'

# Result
print(f"The season for {month} is {season}.")


