#brute force approach using 3 for loop
'''    count=0    
    for i in range(len(arr)):
            res=[]
            for j in range(len(arr)):
                if j != i:
                    res.append(arr[j])
            even_sum=0
            odd_sum=0
            for k in range(len(res)):
                if k%2==0:
                 even_sum+=res[k]   
                else:
                  odd_sum+=res[k]
            if even_sum == odd_sum:
              count+=1
              '''

class Solution:
    def cntWays(self, arr):
        total_even=0
        total_odd=0
        for i in range(len(arr)):
            if i%2==0:
                total_even+=arr[i]
            else:
                total_odd+= arr[i]
    
        count=0
        left_even=0
        left_odd=0
        # Step 2: Try removing each index
        for i in range(len(arr)):
            if i %2 == 0:
                total_even-=arr[i]
            else:
                total_odd-=arr[i]

            if left_even+total_odd == left_odd+total_even:
                count+=1
            
            if i%2 == 0:
                left_even+=arr[i]
            else:
                left_odd+=arr[i]
        return count
        


sol=Solution()
arr=[2, 1, 6, 4]
res=sol.cntWays(arr)
print(res)