# find max uisng range value
arr=[1,2,3,4,5]
max_val=0
for i in range(len(arr)):#iterating 0 to n-1 0,1,2,3,4=5 elemnts
    if max_val < arr[i]:
        max_val=arr[i]
print(max_val)