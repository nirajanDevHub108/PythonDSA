arr=[1,2,3,4,5]
left,right=0 ,len(arr)-1
# we have implemented two pointer and reversed the array
while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(arr)
