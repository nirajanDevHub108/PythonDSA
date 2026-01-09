'''
You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is at most k.

Note: A subarray is a contiguous part of an array.

Examples:

Input: arr[] = [1, 2, 2, 3], k = 2
Output: 9
Explanation: Subarrays with at most 2 distinct elements are: [1], [2], [2], [3], [1, 2], [2, 2], [2, 3], [1, 2, 2] and [2, 2, 3].
        n=len(arr)
        count=0
        for i in range(n):
            st=set()
            for j in range(i,n):
                st.add(arr[j])
                if (len(st) > k):
                    break
                count += 1
        return count
'''
from collections import defaultdict
def countAtMostK(arr, k):
        # Code here
        n=len(arr)
        count=0
        left,right= 0,0
        freq=defaultdict(int)
        while right < n:
            freq[arr[right]] += 1
            
            if freq[arr[right]] == 1:
                k -= 1
        # shrink the window until distinct element
        # count becomes <= k
            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] ==0:
                    k += 1
                left += 1
            count += (right -left +1)
            right+=1
        return count
arr = [1, 2, 2, 3]
k = 2
print(countAtMostK(arr, k))