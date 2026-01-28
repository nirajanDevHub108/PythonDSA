def count_subsets(arr, k):
    count = 0

    def backtrack(index, curr_sum):
        nonlocal count

        # If we've processed all elements
        if index == len(arr):
            if curr_sum == k:
                count += 1
            return

        # Include current element
        backtrack(index + 1, curr_sum + arr[index])

        # Exclude current element
        backtrack(index + 1, curr_sum)

    backtrack(0, 0)
    return count


arr = [1, 2, 3]
k = 3
print(count_subsets(arr, k))  # Output: 2  -> [1,2], [3]
