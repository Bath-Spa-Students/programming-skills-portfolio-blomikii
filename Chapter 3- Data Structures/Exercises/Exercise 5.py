## Exercise 5: Change Guest List

guests = ['Mark John', 'David Jose', 'Maria Theresa', 'Jo Vito']

print (guests[0], "you're invited to my dinner.")
print (guests[1], "you're invited to my dinner.")
print (guests[2], "you're invited to my dinner.")
print (guests[3], "you're invited to my dinner.")

print(guests[0], "can't come anymore.")
del(guests[0])
guests.insert(0, 'Katkat')

print (guests[0], "you're invited to my dinner.")
print (guests[1], "you're invited to my dinner.")
print (guests[2], "you're invited to my dinner.")
print (guests[3], "you're invited to my dinner.")


