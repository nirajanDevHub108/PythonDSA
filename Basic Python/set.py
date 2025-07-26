this_set = {'apple' , "banana" , "cat"}

print(this_set)
''' Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.
'''
# Adding an item to the set
this_set.add("dog")
print(this_set)

# Removing an item from the set
this_set.remove("banana")
print(this_set)

# Checking if an item exists in the set
print("apple" in this_set)

# duplicATION is not allowed 

my_set ={ 1 , 2 , 4, 4, 6, True}

print("it doesnot include duplicate value " ,my_set)

#length of the set
print(len(my_set))

print(type(my_set))

#The set() Constructor we can use set constructor to create a set

set1 = set(('akhil' , 'dabbu ' , ' Niraj'))
print (set1)

#Access Items
for x in my_set:
    print(x)

#Check if "banana" is present in the set:
print ("banana" not in this_set)

'''Add Sets
To add items from another set into the current set, use the update() method'''
this_set.update(my_set)
print(this_set)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

mylist = ["kiwi", "orange"]

this_set.update(mylist)
print(this_set)

this_set.discard("kiwi")
print(this_set)

# using pop method
x = this_set.pop()

print(x)

#The clear() method empties the set:
x =this_set.clear()

#The del keyword will delete the set completely:

del my_set

'''Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

#set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result.
