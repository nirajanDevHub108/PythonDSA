'''
1. brute force approach is to take two loop iterate and take each number subbarray and count the odd number if odd == k then update the count and return the count 
for i in range (n):
        odd = 0
        for j in range(i,n):
            if arr[j] % 2 != 0:
                odd+=1
            
            if odd == k:
                count+=1


2: but if we use hash map to count the freq of odd number track the frequency of prefix subarrays with a given count of odd numbers. For each element, maintain a running count of odd numbers seen so far. If the current odd count is at least k, then the number of subarrays ending at the current index with exactly k odd numbers is equal to prefix[odd - k]. Update the prefix count map as you iterate through the array.


'''

def countSubarrays(arr, k):
    n = len(arr)
    count = 0
    prefix = {0: 1}
    odd = 0
    for i in range(n):

        # if current element is odd
        if arr[i] % 2 != 0:
            odd += 1
        
        if (odd - k) in prefix:
            count += prefix[odd - k]

        prefix[odd] = prefix.get(odd, 0) + 1
    return count


arr = [2, 2, 5, 6, 9, 2, 11]
k = 2
print(countSubarrays(arr, k))