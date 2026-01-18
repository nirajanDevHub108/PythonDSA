def gcd(n1,n2):
    gcd= 1
    for i in range(min(n1,n2),0,-1):
        if n1%i == 0 and n2%i == 0:
            gcd = i
            break
    return gcd
n1=4
n2=6
print(gcd(n1,n2))

'''
java solution

public class Main
{
    public int gcd(int n1,int n2){
        int gcd=1 ;
        
        for (int i =Math.min(n1,n2); i>=1; i--){
            if(n1 % i == 0 && n2 % i == 0){
                gcd = i;
                break;
            }
        }
        return gcd;
    }
	public static void main(String[] args) {
	    int n1 = 4, n2 = 6;
	    Main  m = new Main();
	    
	    int ans = m.gcd(n1,n2);
	    System.out.print(ans);
		
	}
}
'''