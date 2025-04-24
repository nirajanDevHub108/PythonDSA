#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.
myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[1])
print(myList[0])

for x in myList:
    print(x)

#Accessing an index which does not exist generates an exception (an error).
myList1 = [1 , 3 , 5]
myList1[4]
