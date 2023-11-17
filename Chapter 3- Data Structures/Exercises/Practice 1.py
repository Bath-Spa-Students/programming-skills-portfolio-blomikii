'''Given a Python list, write a program to remove all occurrences of item 20.
Given list: list1 = [5, 20, 15, 20, 25, 50, 20]'''

#############################################################################

# Original list
list1 = [5, 20, 15, 20, 25, 50, 20]

# Original list duplicate
original_list = list(list1)

# Removing 20
remove = 20
while remove in list1:
    list1.remove(remove)

# Outputs
print("Original List:")
print(original_list)

print("\nRevised List:")
print(list1) # now modified



