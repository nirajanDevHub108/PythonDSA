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