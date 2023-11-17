'''Write a python program with nested decision structures that perform the following: If amount1 
is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2'''

####################################################################################################

amount_1 = 65
amount_2 = 46

if amount_1 > 10:
    if amount_2 < 100:
        greater_num = max(amount_1, amount_2)
        print(f"The greater number is {greater_num}.")
    else:
        print(f"Amount 2 {amount_2} is not less than 100.")

        