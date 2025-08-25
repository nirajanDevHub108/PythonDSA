#Find the largetst elements in a list
def LargestElement( arr):
    max_val=arr[0]
    for num in arr:
        if num > max_val:
            max_val= num
    
    return max_val
       

arr = [2,7,1,9,3] 

print(LargestElement(arr))

#question2 function to find the smallest element in a list
def smallestElement( arr):
    min_val=arr[0]
    for num in arr:
        if num < min_val:
            min_val= num
    
    return min_val
       

arr = [2,7,1,9,3] 

print(smallestElement(arr))


#Write a function to find the sum of all elemnt in a list