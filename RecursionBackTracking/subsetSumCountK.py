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

'''
java code

class Solution {
    static int count = 0;

    public static int countSubsets(int[] arr, int k) {
        count = 0;
        backtrack(arr, 0, 0, k);
        return count;
    }

    private static void backtrack(int[] arr, int index, int sum, int k) {
        if (index == arr.length) {
            if (sum == k) {
                count++;
            }
            return;
        }

        // Include element
        backtrack(arr, index + 1, sum + arr[index], k);

        // Exclude element
        backtrack(arr, index + 1, sum, k);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        int k = 3;
        System.out.println(countSubsets(arr, k)); // Output: 2
    }
}


'''