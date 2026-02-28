mat = [[1,2,3],[4,5,6]]c
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

# Initializing a 2-D list with values
arr1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

#traversing row
for row in arr1:
     # Traversing each element in the current row
    for x in row:
          print(x,end=" ")
    print()
'''Searching in a Matrix Data Structure:
We can search an element in a matrix by traversing all the elements of the matrix.'''


def search_in_mat(arr2,x):
    row,col=len(arr2),len(arr2[0])
    for i in range(row):
          for j in range(col):
               if arr2[i][j]==x:
                    return True
    return False     
     
x = 12
arr2 = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]

if search_in_mat(arr2,x):
     print("YES")
else:
     print("NO")


#sorting matrix row wise
def sortRows(mat):
    for row in mat:
        row.sort()

mat = [
    [77, 11, 22, 3],
    [11, 89, 1, 12],
    [32, 11, 56, 7],
    [11, 22, 44, 33]
]

sortRows(mat)

print('[\n', end='')
for row in mat:
    print('  [', end='')
    print(', '.join(map(str, row)), end='')
    print(']')
print(']')


#sorting 2d mat by colum wise

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10] 
k = 5

res=(a+b)
res.sort()
print(res[k-1])
