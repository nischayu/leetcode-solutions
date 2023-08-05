class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        alphanumeric = ""

        for char in s:
            if (ord(char) in range(ord('a'), ord('z')+1) or ord(char) in range(ord('0'), ord('9')+1)):
                alphanumeric+= char
        
        print(alphanumeric)
        return alphanumeric == alphanumeric[::-1]  #O(n) time

#The time complexity of this solution is O(n)
#The space complexity of this solution is O(n)