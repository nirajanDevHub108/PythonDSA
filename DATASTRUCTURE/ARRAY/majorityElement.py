'''
Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

Examples:

Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1

[Naive Approach] Using Two Nested Loops - O(n^2) Time and O(1) Space
The idea is to use nested loops to count frequencies. The outer loop selects each element as a candidate, and the inner loop counts how many times it appears. If any element appears more than n / 2 times, it is the majority element.

[Better Approach - 2] Using Hashing - O(n) Time and O(n) Space
The idea is to use a hash map to track frequencies and identify the majority element in a single pass.

Step By Step Implementations:

Initialize an empty hash map.
Traverse the array and update the count of each element.
After each update, check if the count exceeds n / 2.
If found, return that element immediately.
If no such element exists after the loop, return -1.

n = len(arr)
    countMap = defaultdict(int)

    # Traverse the list and count occurrences using the hash map
    for num in arr:
        countMap[num] += 1
        
        # Check if current element count exceeds n / 2
        if countMap[num] > n / 2:
            return num

    # If no majority element is found, return -1
    return -1



'''

def majorityElement(arr):
    n = len(arr)

    majority_count = arr[0]
    votes = 1
    # 1st pass to count majority elemnt
    for i in range (1,n):
        if votes == 0:
            votes +=1
            majority_count = arr[i]
        elif majority_count == arr[i]:
            votes +=1
        else :
            votes -=1
    #2nd pass to verify the candidate
    if arr.count(majority_count) > n//2:

        return majority_count
    else:
        return -1

arr =[2,13]
print(majorityElement(arr))





