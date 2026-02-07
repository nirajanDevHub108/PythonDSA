def maxSum(arr): 
        # Code here
        n = len(arr)

        # Initial sum of array elements
        arrSum = sum(arr)

        # Initial value of i*arr[i]
        currVal = sum(i * arr[i] for i in range(n))

        maxVal = currVal

        # Compute values for other rotations
        for i in range(1, n):
            currVal = currVal + arrSum - n * arr[n - i]
            maxVal = max(maxVal, currVal)

        return maxVal
arr=[8,3,1,2]
print(maxSum(arr))