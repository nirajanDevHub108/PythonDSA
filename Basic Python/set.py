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


#Join Multiple Sets
#All the joining methods and operators can be used to join multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

#myset = set1.union(set2, set3, set4)
myset = set1 | set2 | set3 | set4
print(myset)

'''Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.

The result will be a set.'''

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


#update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection() keep the matching elements 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1.intersection_update(set2)
print(set1)

#Difference
'''The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
#set3 = set1 -set2
print(set3)
set1.difference_update(set2)

print(set1)
#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.


#Symmetric Differences
'''The symmetric_difference() method will keep only the elements that are NOT present in both sets.
You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

'''Method	Shortcut	Description
add()	 	    Adds an element to the set
clear()	 	    Removes all the elements from the set
copy()	 	    Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	        Remove the specified item
intersection()	&	    Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	    Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others'''