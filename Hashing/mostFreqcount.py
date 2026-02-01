def mostFrequentElement(nums):
        freq={}
        n=len(nums)
        max_freq=0
        max_element=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        #checing each element freq in mapp
        for ele,freqency in freq.items():
            if freqency > max_freq:
                max_freq=freqency
                max_element=ele
            elif freqency == max_freq:
                max_element=min(max_element,ele)
        
        return max_element
nums=[1, 2, 2, 3, 3, 3]
print(mostFrequentElement(nums))