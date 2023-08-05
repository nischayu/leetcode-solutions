class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Base Cases
        if(len(s) == 0):
            return 0
        if(len(s) == 1):
            return 1

        #General Case
        left = 0
        right = left + 1
        longest = 1 #1 letter itself
        containSet = set()
        containSet.add(s[left])

        while(left < len(s) and right < len(s)):
            if(s[right] in containSet):
                containSet.remove(s[left])
                left += 1
                
            else:
                containSet.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
                
        
        return longest

        #The time complexity of this solution is O(n)
        #the space complexity of this solution is O(n)