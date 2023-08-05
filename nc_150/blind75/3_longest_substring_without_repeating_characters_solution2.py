class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        containSet= set()
        left = 0
        longest = 0
        for r in range(0, len(s)):
            while(s[r] in containSet):
                containSet.remove(s[left])
                left += 1
            containSet.add(s[r])
            longest = max(longest, r - left + 1)

        return longest

        #The time complexity of this solution is O(n)
        #The space complexity of this solution is O(1)