import array

# Importing the array module

# Creating an array
# Syntax: array(typecode, [elements])
arr = array.array('i', [1, 2, 3, 4, 5])

# Displaying the array
print("Array elements:", arr)

# Accessing elements by index
print("Element at index 0:", arr[0])
print("Element at index 2:", arr[2])

# Adding elements to the array
arr.append(6)
print("Array after appending 6:", arr)

# Inserting an element at a specific position
arr.insert(2, 10)
print("Array after inserting 10 at index 2:", arr)

# Removing an element from the array
arr.remove(3)
print("Array after removing 3:", arr)

# Popping an element from the array
popped_element = arr.pop()
print("Popped element:", popped_element)
print("Array after popping an element:", arr)

# Finding the index of an element
index = arr.index(4)
print("Index of element 4:", index)

# Updating an element
arr[1] = 20
print("Array after updating index 1 to 20:", arr)