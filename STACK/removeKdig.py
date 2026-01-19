def removeKdig( s, k):
        # code here
        n=len(s)
        st=[]
         
        for cur in s:
            while st and k > 0 and st[-1] >cur:
                st.pop()
                k-=1
            if  st or cur != '0':
                st.append(cur)
        while(st and k >0):
            st.pop()
            k-=1
        if not st:
            return "0"
        result = ''.join(st)
        return result

s = "765028321"
k = 5
result = removeKdig(s,k)
print(result)

'''
java code:

/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.Stack;
public class Main
{
    static  String removekdig(String s, int k){
        int n = s.length();
        Stack<Character> st = new Stack<>();
        for(int i =0; i<s.length();++i){
            char c = s.charAt(i);
            
            while(!st.isEmpty() && k > 0 && st.peek() > c){
                st.pop();
                k-=1;
            }
            if(!st.isEmpty() || c !='0'){
                st.push(c);
            }
        }
        while(!st.isEmpty() && k-- > 0){
            st.pop();
        }
        if(st.isEmpty())
            return "0";
        StringBuilder res=new StringBuilder();
        while(!st.isEmpty()){
            res.append(st.pop());
        }
        return res.reverse().toString();
        
    }
    
	public static void main(String[] args) {
	    String s = "765028321";
        int k = 5;
        System.out.println(removekdig(s, k));
		
	}
}

'''