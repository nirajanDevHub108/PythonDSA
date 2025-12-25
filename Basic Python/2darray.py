mat = [[1,2,3],[4,5,6]]
# Print all elements

# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         print(mat[i][j])

#2nd way of fetching row and col item in matrix
for row in (mat):
    for val in (row):
        print(val)

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
left_diagonal=[]
right_diagonal=[]
n=len(mat)
for i in range(len(mat)):
        left_diagonal.append(mat[i][i])
        right_diagonal.append(mat[i][n-i-1])
        
abs_diff=abs(sum(left_diagonal)-sum(right_diagonal))
print(abs_diff)


