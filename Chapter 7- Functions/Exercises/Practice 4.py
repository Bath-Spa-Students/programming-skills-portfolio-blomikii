'''Write a Python program that defines a function to calculate the area of a circle, and 
then calls that function with a given radius.'''

#######################################################################################

# Function
def area(radius):
    pi = 3.14
    return pi*(radius*radius)

# Result
print("Area of circle = %.2f" % area(2));

