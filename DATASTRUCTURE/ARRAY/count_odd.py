def count_odd(arr):
    count=0
    for num in arr:
        if num % 2 !=0:
            count+=1
    return count

arr=[1,2,3,4,5,6]
res=count_odd(arr)
print("odd count is :",res)