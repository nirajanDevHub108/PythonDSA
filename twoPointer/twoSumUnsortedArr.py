#we can solve this two sum in unsorted array using hashmap when indices are required

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap={}
        for i,num in enumerate(nums):
            diffValue=target - num
            if diffValue in hashMap:
                return [hashMap[diffValue],i]
            hashMap[num]=i
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))