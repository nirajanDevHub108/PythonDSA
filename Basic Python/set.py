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