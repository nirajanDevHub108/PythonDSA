class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        count =0
        for i in arr:
            if i % 2 != 0:
                count +=1
        return count
sol=Solution()
n=5
arr=[1,2,3,4,5]
print(sol.countOdd(arr,n))

'''
java code:
class Solution{
    public int countOdd(int[] arr, int n) {
        int count = 0;
        for (int i =0; i<n;i++){
            if ( arr[i ]% 2 != 0){
                count += 1;
            }
        }
        return count;
       
    }
}

'''