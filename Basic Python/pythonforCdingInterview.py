#tips and trick for coding interview
# 
#  
#1.variable are dynamically typed
n=0
print('n =' , n)

n='abc'
print('n =' , n)

#Multiple assignments
n,m = 0, "abc"
n , m , z = 0.123 , "abc" , True

#Increment
n = n + 1 #allowed
n +=1 #allowed

#None is null (absence of value)
n=4
n=None
print(n)

#if statemnet don't need parantheses or curly braces
n=1
if n > 2:
    n -= 1
elif n == 2:
    n *=2
else:
    n+=2

# paranthesis is needed for multi-line conditions
#and = &&
#or = ||

n,m = 1,2
if ((n > 2 and n != m) or n == m):
    n+=1

#while loops are similiar 
# n=0
# while n < 5:
#     print(n)
#     n += 1


# for loop i = 0 to i =4
for i in range(5):
    print(i)
# for loop i = 2 to i =6
for i in range(2,6):
    print(i)

print('_________________')
#division is decimal by default
print(5/2)

print(5 // 2) # double slash round down the decimal part

print( -3 // 2)#most langauge round towards 0 by default so neg numbers will round down

print(int(-3 / 2)) #workaround for rounding towards zero is to use decimal division and then convert to int


print('_________________')

#% modulo is similar
print(10 % 3)

#except for neg values
print(-10 % 3)

import math
print(math.fmod(-10,3))

#more math helper methods
print(math.floor(3 / 2)) #greater value 1 down
print(math.ceil(3 / 2)) #smaller value 2 up
print(math.sqrt(64))
print(math.pow(2,3))

#Max / Min Int
float("inf") #Max
float("-inf")#Min

print(math.pow(2,200))

print(math.pow(2,200) < float("inf"))

#Array in Python is list 
arr =[1, 2, 3]
print(arr)

#dynamic array used as stack
arr.append(4) # add and elemnt in arr
arr.append(5)
print(arr)

arr.pop()#remove the element
print(arr)

arr.insert(1,7) #inserting at particular index
print(arr)

arr[0]=0
arr[3]=0
print(arr)

#initialize arr of size n with default value 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

#last index is fetched by -1
print(arr[-1])

#so on by -2 by second last
print(arr[-2])

#sublist aka slicing
arr=[1, 2, 3, 4]
print(arr[1 : 3]) #forn index 1 included and 3 excluded

#similar to for loop range, last index is non-inclusive
print(arr[0:4])

#unpacking
a, b, c = [1, 2, 3]
print(a , b, c)

# be carefull when you unpack try to match exact with the left hand side variable with right hand side value
a, b = [1, 2]
print(a , b) #thorw error:ValueError: too many values to unpack (expected 2, got 3)

#loop through arr
nums = [1, 2, 3]
#using index
for i in range(len(nums)):
    print(nums[i])

for n in nums: #using value without index
    print(n)

#with index and value
for i , n in enumerate(nums):
    print(i,n)
print("-------------------------")
#looping through multiple array simultaneously with unpacking
nums1=[1, 3, 5]
nums2=[2, 4, 6]

for n1, n2 in zip(nums1,nums2):
    print(n1 , n2)

#revrse using reverse method
nums.reverse()
print(nums)

#sorting using sort method
nums=[2, 3, 4, 1, 5]
nums.sort()
print(nums)

#if you want to print(in decending order) use reverse = True
nums.sort(reverse = True)
print(nums)

#sorting list of string 
arr =["bob", "alice" , "jane" , "doe"]
arr.sort()
print(arr) #by default in alpabetical order

#if we want to do in custome maner then
arr.sort(key= lambda x: len(x))
print(arr)

#List comprehension

arr = [i  for i in range(5)]
print(arr)

#for double the i value
arr = [i+i  for i in range(5)]
print(arr)

#2d -list
arr =[[0] * 4 for i in range(4)]
arr=[[0]*4]*4 #will have to update all the values
print(arr)

#string are similar to arr
s= "abc"
print(s[0:2])

#but they are immutable - we cant modify the value at particular index
#so we can create a new string

s += "def"
print(s)

#valid numeric string conversion
print(int("123") + int("123"))

#and numbers can be converted to string

print(str(123) + str(123))

#incase if we need ASCI value of char we cam do it by using ord

print(ord('a'))
print(ord('A'))

#combine list of string with an empty string delimitor
strings = ["ab", "cd", "ef"]
print("".join(strings))

#Queue in python is double ended queue
from collections import deque #import form collections

queue = deque() 
queue.append(1)#adding to the queue
queue.append(2)
print(queue)

queue.popleft() #best thing is we can remove from the left side
print(queue)

#also append on left side
queue.appendleft(1)
print(queue)

#removing form the queueu
queue.pop()
print(queue)

#adding to the queright
queue.append(2)
print(queue)

#HAsh set  add and search in O(1) time without duplicates

mySet= set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)

print(len(mySet)) #len of set

print (1 in mySet) # true
print (4 in mySet) #false

mySet.remove(2) #remove
print(mySet)

#list to set
print( set([1,2,3]))

#set comprehension

mySet = {i for i in range(5)}
print(mySet)


#Hash MAP aka dict

myMap = {}
myMap["alice"] = 66
myMap["bob"] = 69
print(myMap)
print(len(myMap)) #len of hash map

myMap['alice'] = 80 #chnage the value of key
print(myMap["alice"])

# check if the key is present in map
print("alice" in myMap)
myMap.pop("alice")
print(myMap)

myMap= {"jane" : 70, "max" : 89}
print(myMap)

#dict comprehension
myMap = {i:2 * i for i in range(5)}
print(myMap)

#looping through map
for key in myMap:
    print(key,myMap[key])

#second method for only looping through map values
for val in myMap.values():
    print(val)

for key,val in myMap.items():
    print(key,val)

#Tuples are array but immutable

tup = (1,2,3)
print(tup)

#can be used as a key to hashmap/set
myMap ={ (1,2):3,(4,5):6}
print(myMap)


#Heaps
import heapq

minHeap=[]
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

#min is always as index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

#No max heap by default ,work around  is
# to use min heap and multiply it by -1 when push or pop

maxHeap=[]
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-4)

#max is alwyas at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

#Build heap from initial values of list
arr=[2, 1, 3, 4, 8, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

print('______________________________')
#functions
def myFunc(n, m):
    return n*m

print(myFunc(3,4))

#Nested function have access to other variable

def outer(a,b):
    c = "c"
    def inner():
        return a + b + c
    return inner()
print(outer("a","b"))
