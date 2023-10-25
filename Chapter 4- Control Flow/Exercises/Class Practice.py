# Class Practice

'''drinks = float(input("How many drinks do you need? "))
biscuits = 0
if drinks > 30:
    biscuits = 15
else:
    biscuits = 10
print(f"You get {str(biscuits)} biscuits.")'''

# Nested Decision Structure

'''age = int(input("Please enter your age: "))
job_exp = float(input("How many years of job experience do you have: "))

if age >= 21:
    if job_exp >= 4:
        print("You are eligible for the job interview!")
    else:
        print("You do not have enough experience for this job.")
else: 
    print("You are not old enough for this job.")'''

# If-Elif-Else 

mood=int(input("How are you feeling today? Excited=1, Happy=2, Miserable=3, Nervous=4: "))

if mood==1:
     print("Good for you")
elif mood==2:
     print("Yay!")
elif mood==3:
    print("It's going to be ok.")
elif mood==4:
    print("It'll be fine! No worries.")
else:
     print("Out of Range")

