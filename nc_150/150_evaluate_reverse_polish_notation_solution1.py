class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens) - 1, -1, -1):
            stack.append(tokens[i])

        operations = {'+','-','*','/'}

        popped_array = []
        
        while stack:
            popped = stack.pop()
            if(popped not in operations):
                popped_array.append(int(popped))
            else:
                result = 0
                if(popped == '+'):
                    result = popped_array[-2] + popped_array[-1]
                    
                elif(popped == '-'):
                    result = popped_array[-2] - popped_array[-1]
                elif(popped == '*'):
                    result = popped_array[-2] * popped_array[-1]
                else:
                    result = int(popped_array[-2] / popped_array[-1])
                popped_array = popped_array[:-2]
                popped_array.append(result)
        return popped_array[0]

    #The time complexity of this solution is O(n) where n is len(tokens)
    #The space complexity of this solution is O(n)