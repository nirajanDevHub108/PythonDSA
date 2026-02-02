def largestElement(nums):
        max = nums[0]
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
        return max
nums=[4,5,3,7,1,9]
print(largestElement(nums))

'''
java code;

class Solution {
    public int largestElement(int[] nums) {
        // Arrays.sort(nums);

        // return nums[nums.length - 1];
        //optimal
        int max=nums[0];
        for(int i =1; i<nums.length;i++){
            if( nums[i] > max){
                max = nums[i];
            }
        }
        return max;
    
    }
}
'''