# This program decrements each element of the array by 1 and stores the result in a new list
arr = [54 , 43 , 2 , 1, 5]

ans =[]
n = len(arr)
for i in range (n):
    ans.append(arr[i] - 1)
print(ans)

    