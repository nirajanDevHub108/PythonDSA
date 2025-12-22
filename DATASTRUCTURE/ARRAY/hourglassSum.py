'''Given a  2D array, , an hourglass is a subset of values with indices falling in the following pattern:

a b c  
  d  
e f g
There are  hourglasses in a  array. The  is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in , then print the  hourglass sum.

Example


-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6

maxsum=28
'''
def hourglassSum(arr):
    # Write your code here
    max_sum = float('-inf')  
    for i in range(4):
        for j in range(4):
            hourglass_sum=(arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                            arr[i+1][j+1]+
                            arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            max_sum=max(max_sum,hourglass_sum)
    return max_sum
