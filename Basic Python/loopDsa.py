# find max uisng range value
arr=[1,2,3,4,5]
max_val=0
for i in range(len(arr)):#iterating 0 to n-1 0,1,2,3,4=5 elemnts
    if max_val < arr[i]:
        max_val=arr[i]
print(max_val)

#for each loop is useful when index is not requried like freq count,sum,validation

total=0
for num in arr:
    total+=num
print("total of al number is :",total)