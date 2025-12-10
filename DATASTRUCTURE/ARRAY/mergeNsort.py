class Solution:
    def mergeNsort(self, arr):
        # code here
        # res=list(set(arr1 + arr2))
        # res.sort()
        # return res
        #distinct adjacent array
        m=dict()
        n=len(arr)
        for i in range(n):
            if arr[i] in m:
                m[arr[i]] +=1
            else:
                m[arr[i]] =1
        #storing the max value of lement which occours more
        max=0
        
        for i in range(n):
            if max < m[arr[i]]:
                max=m[arr[i]]
        #prequncy of most occur elm is less than equal to
        #(n+1)//2
        if max > (n+1) // 2:
            return False
        else:
            return True



arr=[1,1,2]
#arr2=[4,3,7,1]

sol = Solution()
result= sol.mergeNsort(arr)
print(result)