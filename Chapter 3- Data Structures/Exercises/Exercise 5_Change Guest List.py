# Exercise 5: Change Guest List

'''You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''

##############################################################################################################

guests = ['Mark John', 'David Jose', 'Maria Theresa', 'Jo Vito']

print (guests[0], "you're invited to my dinner.")
print (guests[1], "you're invited to my dinner.")
print (guests[2], "you're invited to my dinner.")
print (guests[3], "you're invited to my dinner.")

print()

print(guests[0], "can't come anymore.")
del(guests[0])
print("A new guest has been invited!")
guests.insert(0, 'Katherine Lee')

print()

print (guests[0], "you're invited to my dinner.")
print (guests[1], "you're invited to my dinner.")
print (guests[2], "you're invited to my dinner.")
print (guests[3], "you're invited to my dinner.")


