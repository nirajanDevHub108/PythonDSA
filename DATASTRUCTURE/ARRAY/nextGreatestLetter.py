class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for ch in letters:
            if ch > target:
                return ch
            
        return letters[0]

sol=Solution()
letters = ["c","f","j"]
target = "a"
print(sol.nextGreatestLetter(letters,target))

'''
java code:
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        for( char ch: letters){
            if (ch > target){
                return ch;
            }
        }
        return letters[0];
        
    }
}

'''