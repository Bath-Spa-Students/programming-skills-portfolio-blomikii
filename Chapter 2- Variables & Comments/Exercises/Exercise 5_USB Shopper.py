# Exercise 5: USB Shopper

'''A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.'''

#####################################################################################################

cost = 6
money = 50

usb_sticks = 50//6
change = 50%6

print(f"You can buy {usb_sticks} USB sticks with £50, and have £{change} left.")