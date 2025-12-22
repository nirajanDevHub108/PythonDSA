'''You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.

Note:

The array follows 0-based indexing.
The number of rows and columns in the array are denoted by n and m respectively.
Examples:

Input: arr[][] = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
Output: 2
Explanation: Row 2 contains the most number of 1s (4 1s). Hence, the output is 2. 
time complexity=O(nxm)
space=O(1)'''

def rowWithMax1s( arr):
        # code here\maz
        max_count=0
        row_index=-1
        
        for i in range(len(arr)):
            count_ones=sum(arr[i])
            if count_ones > max_count:
                max_count=count_ones
                row_index=i
        return row_index

arr=[[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
res=rowWithMax1s(arr)
print(res)