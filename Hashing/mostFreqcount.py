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

'''
java code:
class Solution {
  public int mostFrequentElement(int[] nums) {
    int n = nums.length;
    int maxfreq = 0;
    int maxElement = 0;

    Map<Integer, Integer> mp = new HashMap<>();

    for (int i = 0; i < n; i++) {
      mp.put(nums[i], mp.getOrDefault(nums[i], 0) + 1);
    }
    for (Map.Entry<Integer, Integer> it : mp.entrySet()) {
      int ele = it.getKey();
      int freq = it.getValue();
      if (freq > maxfreq) {
        maxfreq = freq;
        maxElement = ele;
      } else if (freq == maxfreq) {
        maxElement = Math.min(maxElement, ele);
      }
      
    }
    return maxElement;
  }
}

'''