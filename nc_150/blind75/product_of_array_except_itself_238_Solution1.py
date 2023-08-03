class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Base Case
        if(len(nums) == 2):
            return [nums[1],nums[0]]
        
        #General Case
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)

        prefix[0] = nums[0]
        postfix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]

        for i in range(len(nums)-2,-1, -1):
            postfix[i] = nums[i] * postfix[i+1]

        print(prefix)
        print(postfix)

        for i in range(0, len(nums)):
            if(i == 0):
                output[i] = 1 * postfix[i+1]
            elif(i==len(nums)-1):
                output[i] = prefix[i-1] * 1
            else:
                output[i] = prefix[i-1] * postfix[i+1]

        print(output)
        return output

        #The time complexity of this solution is O(n)
        #The space complexity of this solution is O(n)