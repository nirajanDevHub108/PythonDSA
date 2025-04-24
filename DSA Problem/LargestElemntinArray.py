'''Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 106
'''
def largest(self, arr):
    # code here
    maxItem = arr[0]
    for i in range(0, len(arr)):
        if maxItem > arr[i]:
            maxItem = maxItem
        else:
            maxItem = arr[i]
    return maxItem

# Driver code
if __name__ == "__main__":
    arr = [1, 8, 7, 56, 90]
    print("The largest element is:", largest(None, arr))
    arr = [5, 5, 5, 5, 5]
    print("The largest element is:", largest(None, arr))  

