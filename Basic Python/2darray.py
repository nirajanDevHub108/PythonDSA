mat = [[1,2,3],[4,5,6]]
# Print all elements

# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         print(mat[i][j])

#2nd way of fetching row and col item in matrix
count=0
for row in (mat):
    for val in (row):
        if val >0:
             count+=1
print(count)

mat = [
    [1, 2, -2],
    [4, -5, 6],
    [9, -8, -9]
]
left_diagonal=[]
right_diagonal=[]
n=len(mat)
for i in range(len(mat)):
        left_diagonal.append(mat[i][i])
        right_diagonal.append(mat[i][n-i-1])
        
abs_diff=abs(sum(left_diagonal)-sum(right_diagonal))
print(abs_diff)

#Declaration of a Matrix or two-dimensional array
rows=3
cols=3
row,cols = (3,3)
arr=[[0]*cols]*rows
print(arr)

#initialize a matrix in different languages
# Initializing a 2-D array with values
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
# We can perform a variety of operations on the Matrix Data Structure. Some of the most common operations are:

# Access elements of Matrix
# Traversal of a Matrix
# Searching in a Matrix
# Sorting a Matrix

#1Access elements of Matrix Data Structure:
'''Like one-dimensional arrays, matrices can be accessed randomly by using their indices to access the individual elements. A cell has two indices, one for its row number, and the other for its column number. We can use arr[i][j] to access the element which is at the ith row and jth column of the matrix.'''

print("First element of first row:",arr[0][0])
print("Third element of second row:",arr[1][2])
print("Second element of third row:", arr[2][1])

#Traversal of a Matrix Data Structure:
# We can traverse all the elements of a matrix or two-dimensional array by using two for-loops.