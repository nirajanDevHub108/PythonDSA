def getSecondLargest( arr):
        # Code Here
        second_larget=-1
        largets=arr[0]
        if len(arr)<2:
             return -1
        for num in arr:
               if num > largets:
                    second_larget=largets
                    largets=num
               elif num < largets and num > second_larget:
                     second_larget=num
        return second_larget


arr=[12, 35, 1, 10, 34, 1]
res=getSecondLargest(arr)
print(res)