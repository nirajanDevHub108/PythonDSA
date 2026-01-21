def removeKdig( arr):
        # code here
        n=len(arr)
        span=[0]*n
        st=[]
         
        for i in range(n):
            while st and arr[st[-1]] <=arr[i]:
                st.pop()
            
            if not st:
                span[i] = (i+1)
            else:
                span[i]=(i-st[-1])
            st.append(i)
        return span

arr = [10, 4, 5, 90, 120, 80]
result = removeKdig(arr)
print(result)

'''
java code:

import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class Main
{
    static ArrayList<Integer> calculateSpan(int[] arr) {
        int n= arr.length;
        ArrayList<Integer> span= new ArrayList<>(Collections.nCopies(n,0));
        Stack<Integer> st = new Stack<>();
        for (int i =0;i< n;i++){
            while(!st.isEmpty() && arr[st.peek()] <= arr[i]){
                st.pop();
            }
            if(st.isEmpty()){
                span.set(i,(i+1));
            }
            else{
                span.set(i,(i-st.peek()));
            }
            st.push(i);
            
        }
        return span;
        
    }
    
	public static void main(String[] args) {
	    
	    int[] arr={10, 4, 5, 90, 120, 80};
	    
        System.out.println(calculateSpan(arr));
		
	}
}

'''