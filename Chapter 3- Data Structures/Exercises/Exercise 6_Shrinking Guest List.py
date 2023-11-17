# Exercise 6: Shrinking Guest List

'''•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''

###############################################################################################################

# Inviting guests
guests = ['Mark John', 'David Jose', 'Maria Theresa']

# Using for loop
for name in guests:
    print(f"{name}, you're invited to my dinner.")

print()

# New guest invited 
print(guests[0], "can't come anymore.")
del(guests[0])
print("A new guest has been invited!")
guests.insert(0, 'Katherine Lee')

print()

# Using for loop
for name in guests:
    print(f"{name}, you're invited to my dinner.") 

print()

# Invite more guests
print("More people can come to dinner!\n")

guests.append('Joe Ando')
guests.append('Toto Wolff')
guests.append('Mario Paul')

# Using for loop
for name in guests:
    print(f"{name}, you're invited to my dinner.") 

print()

# Cancel invitations
print("Apologies! Only two people can come to the dinner.\n")

# Using for loop
for name in guests[:4]:
    removed_guest = guests.pop()
    print(f"{removed_guest}, sorry. You can't come to dinner.")

print()

# Keep two guests
print(guests[0], "you're still invited to my dinner.")
print(guests[1], "you're still invited to my dinner.")

# Empty out the list

del(guests[0])
del(guests[0])

# Empty list
print(guests)

