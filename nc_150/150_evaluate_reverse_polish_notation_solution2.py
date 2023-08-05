class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if(char == '+'):
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif(char == '-'): #order matters
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif(char == '*'):
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif(char == '/'): #order matters
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(char))

        #guaranteed to have one remaining item in stack
        return stack[0]

    #The time complexity of this solution is O(2n) #because we append to stack and pop from stack
    #The space complexity of this solution is O(n) because it's just the stack