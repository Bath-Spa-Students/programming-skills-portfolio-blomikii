# Exercise 7: Favorite Places

''' Think of at least five places in the world you’d like to visit.

Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
Use sorted() to print your list in alphabetical order without modifying the actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
Show that your list is still in its original order by printing it again.
Use reverse() to change the order of your list. Print the list to show that its order has changed.
Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed. '''

##############################################################################################################

# List of Places
places = ['Switzerland', 'South of France', 'Monaco', 'Germany', 'Japan', 'Thailand']

# Original Order
print("Original Order:\n", places)

# Alphabetical Order
print("\nAlphabetical Order:\n", sorted(places))

# Original Order
print("\nOriginal Order:\n", places)

# Reverse Alphabetical Order
print("\nReversed Alphabetical Order:\n", sorted(places, reverse=True))

# Original Order
print("\nOriginal Order:\n", places)

# Reverse Order
places.reverse()
print("\nReversed Order:\n", places)

# Original Order
places.reverse()
print("\nOriginal Order:\n", places)

# Alphabetical Order
places.sort()
print("\nAlphabetical Order:\n", places)

# Reverse Alphabetical Order
places.sort(reverse=True)
print("\nReversed Alphabetical Order:\n", places)
