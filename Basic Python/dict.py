'''Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.'''

this_mydict ={
    "brand" : "Ford",
    "model" : "mustang",
    "year "  : 1974,
    "year " : 2017

}
print(this_mydict)
print(len(this_mydict))

'''Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

'''
print(this_mydict["brand"])

#dictonary can have any data type String, int, boolean, and list data types:

dic2 = {
    "brand" : "Ford",
    "model" : "mustang",
    "electric" : False,
    "year "  : 1974,
    "colors" : ['red ', 'blue' ,'black']

}
print(dic2)
print(type(dic2))

#dictonary constructor
this_dict = dict(name = "akhil " , age = 23 , sex ="male " , country = "Nepal")
print(this_dict)

#accessing the dictonary item

model = dic2.get("model")
print(model)

#The keys() method will return a list of all the keys in the dictionary.
m = dic2.keys()
print(m)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

x = dic2.values()

#The items() method will return each item in a dictionary, as tuples in a list.

x = dic2.items()
print(x)

if "model" in dic2:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

this_dict['role'] = "sales force developer"
print(this_dict)

'''Update Dictionary
The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.'''

#Removing Items
#There are several methods to remove items from a dictionary:

#The pop() method removes the item with the specified key name:

this_dict.pop("age")
print(this_dict)

#The popitem() method removes the last inserted item 

#The del keyword removes the item with the specified key name:

del this_dict ["sex"]
print(this_dict)

#The clear() method empties the dictionary:

this_dict.clear()

#for 
#Print all key names in the dictionary, one by one:
for x in this_dict:
  print(x)

#Print all values in the dictionary, one by one:
for x in this_dict:
  print(this_dict[x])

#You can also use the values() method to return values of a dictionary:
for x in this_dict.values():
  print(x)

#You can use the keys() method to return the keys of a dictionary:
for x in this_dict.keys():
  print(x)
