def returnUniqueElemnt(arr):
    n=len(arr)
    ans=0
    for i in range(n):
         #if we xor using same number it will give you 0 and 0 with diffrent number will give you other number
         ans=arr[i]^ans
    return ans

arr=[2,3,4,2,3]
res=returnUniqueElemnt(arr)
print(res)
