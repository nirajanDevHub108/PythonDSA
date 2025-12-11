#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.
'''myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[1])
print(myList[0])

for x in myList:
    print(x)

Accessing an index which does not exist generates an exception (an error).
myList1 = [1 , 3 , 5]
myList1.append ([5,6,7,8])
print(myList1)


a = [1, 2, 3, 4, 5] 
b = a  #1,2,3,4,5
b[0] = 0; #0,2,3,4,5

print(a)  #0,2,3,4,5

a = [1998, 2002] 
b = [2014, 2016] 

print ((a + b)*2) # 1998,2002,2014,2016,1998,2002,2014,2016
'''

#Using for Loop with range()
a = [1, 2, 3, 4, 5] 
n = len(a)# get the length  list a

#for i in range (n):
    #print(a[i])

#Using while Loop
# i = 0
# while i < n:
#     print(a[i])
#     i += 1

'''Using enumerate()
#We can also use the enumerate() function to iterate through the list. #This method provides both the index (i) and the value (val) of each element during the loop.'''

# for i , val in enumerate(a):
#     print(f"Index: {i}, Value: {val}")

#nested list is a list having more lists in it

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Accessing elements in a nested list at row 2 and colum 3
# print(matrix[1][2])

'''List Comprehension in Python
List comprehension is a concise way to create lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as a list or range.'''

# squares =[x ** 2 for x in range(10)]
# print(squares)

arr=[10,20,30,40]
print(arr[-2])
#printing all element
# for i in arr:
#     print(i)

#print index wise
#counting the elements
count=0
for i in range(len(arr)):
    # print(f" index :{i} ,{arr[i]}")
    count+=1
    print(arr[-1])
print(count)