'''Write a python program with if statement that assigns 20 to the variable y and assigns 40 to the 
variable z if the variable & is greater than 100.'''

####################################################################################################

x = int(input("Enter a number: "))

if x > 100:
    y = 20
    z = 40
    print(f"Variables assigned: y={y} | z={z}")
else:
    print("Conditions not met.")

