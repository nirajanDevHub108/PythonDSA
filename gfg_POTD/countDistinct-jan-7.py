'''
Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
Explanation:
First window is [1, 2, 1, 3], count of distinct numbers is 3.
Second window is [2, 1, 3, 4] count of distinct numbers is 4.
Third window is [1, 3, 4, 2] count of distinct numbers is 4.
Fourth window is [3, 4, 2, 3] count of distinct numbers is 3.
'''

from collections import defaultdict
def countDistinct(arr,k):
  
    freq = defaultdict(int)
    res=[]

    # 1st block of k
    for i in range(k):
        freq[arr[i]] += 1
    res.append(len(freq))

    #now from index 2 to length or arr
    for i in range(k,len(arr)):
        freq[arr[i]] += 1
        freq[arr[i-k]] -= 1

        if freq[arr[i-k]] == 0:
            del freq[arr[i-k]]
        res.append(len(freq))

    return res

arr= [1, 1, 1, 1, 1]
k = 3
print(countDistinct(arr,k))
