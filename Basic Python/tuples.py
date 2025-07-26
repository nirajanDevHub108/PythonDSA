'''Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.'''

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5 ,4 ,4,4)
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

#Loop Through the Index Numbers
for i in range (len(my_tuple)):
    print("Item at index", i, "is", my_tuple[i])

#Using a While Loop
print("Using a while loop to iterate through the tuple:")
i = 0
while i < (len(my_tuple)):
   print("Item at index", i, "is", my_tuple[i])
   i+=1


#Unpacking a Tuple
'''When we create a tuple, we normally assign values to it. This is called "packing" a tuple:'''
packed_tuple = (1, 2, 3)
# Unpacking a tuple into variables
a, b, c = packed_tuple
print("Unpacked values:", a, b, c)

#example-2 of unpacking 
fruits = ("apple", "banana", "cherry")
# Unpacking the tuple into variables
x , y , z = fruits
print("Unpacked fruits:", x, y, z)

# Using the * operator to unpack a tuple Using Asterisk*
# Unpacking with the * operator
numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers  # a will be 1, b will be [2, 3, 4], c will be 5 value of variable b with * will be assigned as a list
print("Unpacked numbers:", a, b, c)

#Join Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

joined_tuple = tuple1 + tuple2  # Joining two tuples
print("Joined tuple:", joined_tuple)

# Multiply Tuples
multiplied_tuple = tuple1 * 2  # Multiplying a tuple   
print("Multiplied tuple:", multiplied_tuple)

# Count Occurrences of an Item
count_of_4 = my_tuple.count(4)  # Counting occurrences of item 4
print("Count of 4 in tuple:", count_of_4)