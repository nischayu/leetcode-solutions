class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {')':'(', '}':'{', ']':'['}
        #Base Case
        if(len(s)%2==1):
            return False
        
        stack = []
        for i in range(0, len(s)):
            if(s[i] in brackets_map.values()): #opening bracket encountered
                stack.append(s[i])
            else: #closing bracket encountered
                if(len(stack)==0):
                    return False
                popped = stack.pop() #will be the opening bracket.
                if(brackets_map[s[i]] != popped):
                    return False
                        
        if(len(stack) == 0):
            return True
        return False

#The time complexity of this solution is O(n)
#The space complexity of this solution is O(1)
#maybe not the most efficient code tho