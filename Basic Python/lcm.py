def LCM(n1, n2):
        lcm=1
        n=max(n1,n2)
        i=1
        while True:
            mul= i * n
            if mul % n1 == 0 and mul % n2 == 0:
                lcm = mul
                break
            i+=1
        return lcm
n1=3
n2=5
print(LCM(n1,n2))

'''
java colution:
class Solution {
    public int LCM(int n1, int n2) {
        int lcm=1;
        int n = Math.max(n1,n2);
        int i =0;
        while (true){
            int mul = i * n;
            if (mul % n1 == 0 && mul % n2 ==0){
                lcm = mul;
                break;
            }
            i++;
        }
        return lcm

    }
}

optimal approach:
The optimal way to find LCM to two numbers is by finding their GCD and using the formula:
lcm(n1, n2) = (n1 * n2) / gcd(n1, n2).

def GCD(self,n1,n2):
        while n1 > 0 and n2 > 0:
            if n1 > n2 :
                n1=n1 % n2
            else:
                n2=n2 % n1
        if n1 == 0:
            return n2
        return n1

    def LCM(self, n1, n2):
        gcd=self.GCD(n1,n2)

        lcm = (n1* n2 )// gcd
        
        return lcm
        
        
java code optimal code:
class Solution {
    public int LCM(int n1, int n2) {
        int result= (n1 * n2) /Gcd(n1,n2);
        return result;

    }
    private int Gcd(int n1,int n2){
        while( n1 >0 && n2 >0){
            if(n1 >n2 ) n1= n1 % n2;
            else{
                n2 = n2 % n1;
            }
        }
        if(n1 == 0) return n2;
        else{
            return n1;
        }

    }
}
'''