'''Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that 
copies the values in numbers to numbers2.'''

##############################################################################################

numbers1 = [1, 2, 3, 4, 5, 6 , 7 ,8 , 9, 10]
numbers2 = numbers1[:] #list slicing

print(numbers2)

