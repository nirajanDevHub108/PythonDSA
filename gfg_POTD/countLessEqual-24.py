def countLessEqual(arr, x):
        count=0
        for num in arr:
            if num <= x:
                count+=1
        return count

arr=[6, 10, 12, 15, 2, 4, 5]
x = 14
res=countLessEqual(arr,x)
print(res)