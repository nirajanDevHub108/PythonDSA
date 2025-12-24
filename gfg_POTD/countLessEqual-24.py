'''
Given a sorted array arr[] containing distinct positive integers that has been rotated at some unknown pivot, and a value x. Your task is to count the number of elements in the array that are less than or equal to x.

Examples:

Input: arr[] = [4, 5, 8, 1, 3], x = 6
Output: 4
Explanation: 1, 3, 4 and 5 are less than 6, so the count of all elements less than 6 is 4.
      
Brute force solution is having O(n) Tc we need to optimize it using binary search implemented array i O(logn) Tc 
        count=0
        for num in arr:
            if num <= x:
                count+=1
        return count'''

def findPivot(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low  

def countLE(arr, x, low, high):
    start = low      # store original low
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans - start + 1 if ans != -1 else 0
     
def countLessEqual(arr, x):
    n = len(arr)
    pivot = findPivot(arr)

    count = 0

    # Left sorted part
    if pivot > 0 and arr[0] <= x:
        count += countLE(arr, x, 0, pivot - 1)

    # Right sorted part
    if arr[pivot] <= x:
        count += countLE(arr, x, pivot, n - 1)

    return count



arr=[6, 10, 12, 15, 2, 4, 5]
x = 14
res=countLessEqual(arr,x)
print(res)