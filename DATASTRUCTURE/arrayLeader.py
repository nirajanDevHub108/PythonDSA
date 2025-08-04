'''
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
'''	
arr= [16, 17, 4, 3, 5, 2]
n = len(arr)
res =[]
max_fromRight = arr[-1] # taking the last elemnet as it is leader always
res.append(max_fromRight) # adding it in new array list
for i in range (n -2 ,-1 ,-1): #traversing from secondlast index to the 0th index
    if arr[i]  >= max_fromRight: #checking if index value is greater thanor equal to max 
        max_fromRight = arr[i]
        res.append(arr[i]) #appending it in the res array

res.reverse() #reversing the res array to get the actual leader
print(res)