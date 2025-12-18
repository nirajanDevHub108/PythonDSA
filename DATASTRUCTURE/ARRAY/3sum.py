class Solution:
    def three_sum(self, arr):
        res=[]
        n=len(arr)
        arr.sort()
        for i in range(n-2):
            if i>0 and arr[i]==arr[i-1]:
                continue
                
            a=arr[i]
            left,right=i+1 ,n-1
            while left <right:
                sum = a+arr[left]+arr[right]
                if  sum == 0:
                    res.append([a,arr[left],arr[right]])
                    left+=1
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    right -=1

        return list(set(tuple(sorted(triplet)) for triplet in res))
sol=Solution()
arr=[1,-1,-1,0]
res=sol.three_sum(arr)
print(res)


'''for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==0:
                        res.append(sorted([arr[i], arr[j], arr[k]]))
        return list(set(tuple(sorted(triplet)) for triplet in res))'''