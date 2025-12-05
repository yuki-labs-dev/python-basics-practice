# Basic Python practice from DataCamp Intro to Python

# Variables & numeric operations
a = 7
b = 2.5
result = a * b
print(result)

# Strings
greeting = "Hello, Python!"
print(greeting.upper())
print(len(greeting))

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Indexing and slicing
print(fruits[0])
print(fruits[1:3])

# Modify a list
fruits.append("orange")
print(fruits)

# Using NumPy for simple numerical operations
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)

# Basic NumPy operations
print("Mean:", np.mean(array))
print("Sum:", np.sum(array))
print("Squared values:", array ** 2)
