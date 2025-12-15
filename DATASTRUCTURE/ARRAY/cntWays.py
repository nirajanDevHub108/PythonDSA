#brute force approach using 3 for loop
'''        for i in range(len(arr)):
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
        count=0

        return count

sol=Solution()
arr=[2, 1, 6, 4]
res=sol.cntWays(arr)
print(res)