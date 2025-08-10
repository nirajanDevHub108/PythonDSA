'''You are given a list arr that contains integers. You need to count distinct integers in list.

Examples:

Input: arr = [4, 4, 5, 4, 3, 8, 4, 2, 4, 8, 1, 7]
Output: 7
Explanation: The distinct list would be [4, 5, 3, 8, 2, 1, 7]. The length is 7'''



def countDistinct( arr):
        #code here 
        count =0
        arr.sort()
        
        for i in range(len(arr)):
            if i ==0 or arr[i] != arr[i-1]:
                count +=1
        return count

arr = [2, 3, 4, 5, 1, 2, 14, 6, 8, 7, 5]
print(countDistinct(arr))