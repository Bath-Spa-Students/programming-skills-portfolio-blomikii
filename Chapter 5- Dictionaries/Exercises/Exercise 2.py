# Exercise 2

glossary = {
    "Tuples" : "A tuple is an ordered, and unchangeable, collection.",
    "Operators" : "Operators are used to perform operations on variables and values.",
    "String" : "Arrays of bytes representing unicode characters.",
    "Variable" : "Variables are containers for storing data values.",
    "Array" : "Arrays are used to store multiple values in one single variable:"
}

for word, definition in glossary.items():
    print(f"{word} : \n{definition}\n")