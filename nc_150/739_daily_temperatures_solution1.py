class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            if not stack: #stack empty
                stack.append((temperatures[i], i)) #(temperature, index)
            else:
                lesser = True
                while lesser:
                    if not stack or temperatures[i] <= stack[-1][0]:
                        stack.append((temperatures[i], i))
                        lesser = False
                    if(temperatures[i] > stack[-1][0]): #stack[-1] gets top element in stack
                        popped = stack.pop()
                        output[popped[1]] = i - popped[1]
        return output

	#The time complexity of this solution is O(n)
  #The space complexity of this solution is O(n)