# Exercise 3

glossary = {
    "Tuples" : "A tuple is an ordered, and unchangeable, collection.",
    "Operators" : "Operators are used to perform operations on variables and values.",
    "String" : "Arrays of bytes representing unicode characters.",
    "Variable" : "Variables are containers for storing data values.",
    "Array" : "Arrays are used to store multiple values in one single variable:",
    "Function" : "A reusable block of code that performs a specific task or set of tasks. Functions are called to execute their code.",
    "Dictionary" : "A data structure that stores key-value pairs. It allows you to access values by using their corresponding keys.",
    "Boolean" : "Referring to a way of using 0 (for false) and 1 (for true) in algebraic notation to represent logical statements.",
    "Int" : "The integer number type",
    "Comments" : "Comments are code lines that will not be executed"

}

for word, definition in glossary.items():
    print(f"{word}: \n{definition}\n")