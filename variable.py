#number 
#Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals). (It also supports complex numbers)
#
myInt = 10

print( myInt)

#To define a floating point number, you may use one of the following notations:

myFloat = 10.5
print (myFloat)
myFloat =float(10)
print (myFloat)

#Strings

#Strings are defined either with a single quote or a double quotes.

myString = "Hello World"
print (myString)
myString = 'hello'
print (myString)

#The difference between the two is that using double quotes makes it easy to include apostrophes 
# (whereas these would terminate the string if using single quotes)

myString = "It's a beautiful day"
print (myString)

#Simple operators can be executed on numbers and strings:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# % for modulus
# ** for exponentiation
# // for floor division
# + for concatenation
# - for repetition

myint = 10
two =2
sum = myint + two
print (sum)

#atring example
myString = "hello "
myString2 = "World"
myString3 = myString + myString2
print (myString3)

#String repetition
myString = "hello "
myString2 = myString * 3
print (myString2)

#String slicing
#Python supports slicing of strings. For example:
myString = "hello world"
print (myString[0:5]) #hello

print (myString[6:]) #world

#Python also supports negative indexing. For example:
myString = "hello world"
print (myString[-1]) #d

#Python also supports string formatting. For example:
myString = "hello world"
myString2 = "hello %s" % myString
print (myString2) #hello hello world

#Python also supports string formatting with the format() method. For example:  
myString = "hello world"
myString2 = "hello {}".format(myString) 
print (myString2) #hello hello world

#Python also supports string formatting with f-strings. For example:
myString = "hello world"
myString2 = f"hello {myString}"
print (myString2) #hello hello world

