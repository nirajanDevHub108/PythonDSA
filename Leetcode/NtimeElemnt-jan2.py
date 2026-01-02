def repeatedNTimes(nums):
    n= len(nums)// 2
    freq={}
    for num in nums:
        freq[num]=freq.get(num,0)+1
        if freq[num] == n:
            return num
nums=[1,2,3,3]
print(repeatedNTimes(nums))

'''
        n = len(nums) // 2
        for i in nums:
            if nums.count(i) == n:
                return i
                '''