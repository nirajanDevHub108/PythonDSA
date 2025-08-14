'''Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Method one using sorted string if both are same means true else false 
    def isAnagram(self , s:str ,t:str )-> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t) #Tc = O(nlog n + m log m)
                                    #space complexity =O(1) or O(n + m)
    # method 2 using HAsh map
        def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS , countT ={} ,{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i] , 0)
            countT[t[i]] = 1 + countT.get(t[i] , 0)
        return countS == countT
        Time complexity = O(n+m) space (1)
    
    #method 3 Hash Table (Using Array)
'''
class Solution:
    def isAnagram(self , s:str ,t:str )-> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

sol = Solution()
print(sol.isAnagram("ama","maa"))