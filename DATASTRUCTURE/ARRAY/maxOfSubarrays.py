'''
1.brute force: is to use two for loop take max as a 1st elemnt and verify for k size sub array and compare if arr[j] value is greater than max then we cn update the max and add it to res. tc O ( n*k)
for i in range( n - k + 1):
        current_max=arr[i]
        for j in range(i,i+k):
            if arr[j] > current_max:
                current_max= arr[j]
        res.append(current_max)
    return res

2.optimal approach is to use deque Create a Deque, dq of capacity k, that stores only useful elements of current window of k elements. An element is useful if it is in current window and is greater than all other elements on right side of it in current window. Process all array elements one by one and maintain dq to contain useful elements of current window and these useful elements are maintained in sorted order. The element at front of the dq is the largest and element at rear/back of dq is the smallest of current window.

'''
from collections import deque
def maxOfSubarrays(arr, k):
    n=len(arr)
    res=[]
    deq=deque()
    
    for i in range(n):
        if deq and deq[0] <= i-k:
            deq.popleft()
            
        while deq and arr[deq[-1]] < arr[i]:
            deq.pop()
        deq.append(i)
        
        if i >= k - 1:
            res.append(arr[deq[0]])
    return res   
    

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3

print(maxOfSubarrays(arr, k))
