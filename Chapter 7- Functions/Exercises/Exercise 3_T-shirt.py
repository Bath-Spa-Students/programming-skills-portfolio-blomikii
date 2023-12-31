# Exercise 3: T-shirt

''' Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

###############################################################################################################

def make_shirt(size, text):
    print(f"The size of my t-shirt is {size}.")
    print(f'It has a message saying, "{text}".')

make_shirt('extra small', 'Rock On')
make_shirt(size='medium', text='You light up my world <3')

