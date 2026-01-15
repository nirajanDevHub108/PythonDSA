'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array arr[]. You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating than their neighbors get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute.

Note: The answer will always fit into a 32-bit integer.

Examples:

Input: arr[] = [1, 0, 2]
Output: 5
Explanation: Children at index 0 and 2 will get 2 candies each as their rating is higher than index 1, and index 1 will get 1 candy. Thus total candies = 2 + 1 + 2 = 5.
'''
import array
def minCandy(arr):
    n=len(arr)
    leftCandy=array.array('i',[1]*n)
    rightCandy=array.array('i',[1]*n)
    
    #left traversal
    for i in range (1,n):
        if arr[i] > arr[i-1]:
            leftCandy[i]=leftCandy[i-1]+1
    # righttraversal
    for i in range (n-2,-1,-1):
        if arr[i] > arr[i+1]:
            rightCandy[i]=rightCandy[i+1]+1 
    return sum(max(leftCandy[i],rightCandy[i]) for i in range(n) )   

arr = [3 ,5 ,0, 1, 0, 1]
print(minCandy(arr))