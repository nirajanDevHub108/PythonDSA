'''Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.'''

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5 ,4)
print("Tuple:", my_tuple)

# lengrth of tuple
length =len(my_tuple)
print("Length of tuple:", length)

this_tuple =("apple", "banana", "cherry")
print("Single item tuple:", this_tuple)

#tuple can have any data type
tuple1 = ("abc", 34, True, 40, "male")
print("Mixed data types tuple:", tuple1)

#tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))
print("Tuple using constructor:", thistuple)

#Access Tuple Items by refering the index
print("First item in tuple:", my_tuple[0])  # Accessing first item
print("Last item in tuple:", my_tuple[-1])  # Accessing last item

#Range of Indexes
print("Items from index 1 to 3:", my_tuple[1:4])  # Accessing items from index 1 to 3

print("Items from start to index 2:", my_tuple[:3])  # Accessing items from start to index 2

print("Items from index 2 to end:", my_tuple[2:])  # Accessing items from index 2 to end

#Range of Negative Indexes
print("Items from index -4 to -1:", my_tuple[-4:-1])  # Accessing items from index -4 to -1

#Check if Item Exists
if 3 in my_tuple:
    print("3 is present in my tuple")

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change Tuple Values
'''Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.'''

# Convert tuple to list, change the list, and convert back to tuple
my_tuple_list = list(my_tuple)  # Convert tuple to list
my_tuple_list[0] = 10  # Change the first item
my_tuple = tuple(my_tuple_list)  # Convert list back to tuple
print("Tuple after changing first item:", my_tuple)

#add item in tuple
my_tuple_list = list(my_tuple)  # Convert tuple to list
my_tuple_list.append(6) # Add a new item
my_tuple = tuple(my_tuple_list) # Convert list back to tuple
print("Tuple after adding new item:", my_tuple)

# Remove Item from Tuple
my_tuple_list = list(my_tuple)  # Convert tuple to list
my_tuple_list.remove(4) # Remove the item
my_tuple = tuple(my_tuple_list)  # Convert list back to tuple
print("Tuple after removing item:", my_tuple)

#looping through the tuple 
for item in my_tuple:
   print("Item in tuple:", item)

#Unpacking a Tuple
'''When we create a tuple, we normally assign values to it. This is called "packing" a tuple:'''