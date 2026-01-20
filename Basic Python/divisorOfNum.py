class Solution:
    def divisors(self, n):
        i=1
        res=[]
        while i <= n:
            if n % i == 0:
                res.append(i)
            i+=1
        return res
n=6
sol=Solution()
print(sol.divisors(n))

'''
java code:
class Solution {
    public int[] divisors(int n) {
        ArrayList<Integer> res= new ArrayList<>();
        int i = 1;
        while ( i <= n){
            if(n % i == 0){
                res.add(i);
            }
            i++;
        }
        int[] result = new int[res.size()];
        for(int j =0; j< res.size(); j++){
                result[j]=res.get(j);
        }
        return result;

    }
}

'''