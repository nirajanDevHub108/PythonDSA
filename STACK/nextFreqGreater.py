def nextFreqGreater(arr):
        # code here
        n = len(arr)
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        res=[-1]*n
        st=[]
        
        for i in range(n):
            
            while st and freq[arr[i]] > freq[arr[st[-1]]]:
                res[st.pop()]=arr[i]
            st.append(i)
        return res

arr = [2, 1, 1, 3, 2, 1]
result = nextFreqGreater(arr)
print(result)

'''
java code 

import java.util.Stack;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Map;
import java.util.ArrayList;
public class Main
{
        public static ArrayList<Integer> nextGreaterFreq(int[] arr){
            int n = arr.length;
            Map<Integer,Integer> freq= new HashMap<>();
            for (int num : arr){
                freq.put(num,freq.getOrDefault(num,0)+1);
            }
            int [] res = new int[n];
            Arrays.fill(res,-1);
            Stack<Integer> st = new Stack<>();
            
            for (int i =0;i < n; i++){
                
                while (!st.isEmpty() && freq.get(arr[i]) >
                         freq.get(arr[st.peek()])){
                             res[st.pop()] = arr[i];
                         }
                st.push(i);
            }
            
            ArrayList<Integer> result = new ArrayList<>();
            for ( int x : res){
                result.add(x);
            }
            return result;
            
            
            
        }
	public static void main(String[] args) {
	    int[] arr = {2, 1, 1, 3, 2, 1};
	    
		ArrayList<Integer> result = nextGreaterFreq(arr);
		for ( int x : result){
		    System.out.print(x + " ");
		}
	}
}

'''