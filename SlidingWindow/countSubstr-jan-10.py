'''
1.brute force is to take two loop and set to count all substring distinct sequence and if len(set) == k increase the count
n=len(s) tc-O(n^2)
        count=0
        
        for i in range(n):
            st=set()
            for j in range(i,n):
                st.add(s[j])
                
                if (len(st) == k) :
                    count +=1
        return count

2,optimal approach tc O(n) - Sliding window techinuqe
The idea is to use sliding window technique to efficiently count substrings with at most k distinct characters, and then subtract the count of substrings with at most k-1 distinct characters to obtain the number of substrings with exactly k distinct characters.


'''
from collections import defaultdict

def countSubstr(s, k):
        # Code here
        def atMostK(k):
            if k < 0:
                return 0
            count=0
            left=0
            freq=defaultdict(int)
            for right in range(len(s)):
                freq[s[right]] +=1
                
                while len(freq) > k:
                    freq[s[left]] -=1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                count += right - left + 1
            return count
        return atMostK(k) - atMostK(k - 1)
            
        
        
s="abc"
k = 2
print(countSubstr(s,k))