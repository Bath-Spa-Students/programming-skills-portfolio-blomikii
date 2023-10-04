## Exercise 6: Shrinking Guest List

guests = ['Doyoung', 'Lisa', 'Eric']

print("Only two people can come to the dinner.")

print("Sorry", guests[2], ",you can no longer come to the dinner.")
guests.pop()


print(guests[0], "you're still invited to my dinner.")
print(guests[1], "you're still invited to my dinner.")

del guests

print(guests)


