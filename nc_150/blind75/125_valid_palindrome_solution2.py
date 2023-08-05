class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while(left < right):
            #get valid left
            while(left < right and not self.alphaNum(s[left])):
                left += 1
            #get valid right
            while(left < right and not self.alphaNum(s[right])):
                right -= 1

            #comparison
            if(s[left].lower() != s[right].lower()):
                return False
            #comparison passed, adjust left and right
            left += 1
            right -= 1
        return True
        

    def alphaNum(self, char):
        return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')

    #The time complexity of this solution is O(n)
    #The space complexity of this solution is O(1)