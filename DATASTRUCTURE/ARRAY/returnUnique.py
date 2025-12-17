def returnUniqueElemnt(arr,k):
        n=len(arr)
        ans=0
        max_num=max(arr)
        max_bit=max_num.bit_length()
        for bit in range(max_bit):
            count=0
            for num in arr:
                if (num >> bit) &1:
                    count+=1
            if count % k != 0:
                ans |=(1<<bit)
          
        return ans
    # ans=0
    # for i in range(n):
    #      #if we xor using same number it will give you 0 and 0 with diffrent number will give you other number
    #      ans=arr[i]^ans
    # return ans

arr=[6, 2, 5, 2, 2, 6, 6]
k=3
res=returnUniqueElemnt(arr,k)
print(res)
