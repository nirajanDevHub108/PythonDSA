from collections import Counter
def count_subsets(arr, k):
        n = len(arr)
        mid = n // 2
    
        left = arr[:mid]
        right = arr[mid:]
    
        def subset_sums(nums):
            sums = [0]
            for x in nums:
                sums += [s + x for s in sums]
            return sums
    
        left_sums = subset_sums(left)
        right_sums = subset_sums(right)
        
        right_counter= Counter(right_sums)
    
        count = 0
        for s in left_sums:
            
            count += right_counter[k-s]
    
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