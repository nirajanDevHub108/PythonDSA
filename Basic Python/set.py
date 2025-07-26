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