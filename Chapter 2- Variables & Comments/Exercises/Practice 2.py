'''Write a python program that takes courses marks as input and then calculates average of all the 
courses. After calculating the average, calculate the percentage of a student using total marks. Assume 
the total of all the courses marks is 500 or take the total marks from the user as input.'''

##############################################################################################################

print("Enter your marks for your courses\n")

# Input for course marks
course_1 = int(input("Course 1: "))
course_2 = int(input("Course 2: "))
course_3 = int(input("Course 3: "))
course_4 = int(input("Course 4: "))
course_5 = int(input("Course 5: "))

# Total marks
total_marks = course_1 + course_2 + course_3 + course_4 + course_5
print(f"Total Marks: {total_marks}/500")

# Average
average = total_marks / 5
print(f"Average: {average:.2f}")

percentage = (total_marks / 500) * 100
print(f"Percentage: {percentage:.2f}%")




