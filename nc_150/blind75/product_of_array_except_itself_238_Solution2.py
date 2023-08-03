class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Base Case
        if(len(nums) == 2):
            return [nums[1],nums[0]]
        
        #General Case
        prefix = 1
        postfix = 1
        output = [1] * len(nums)

        for i in range(0, len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

#The time complexity of this solution is O(n)
#The space complexity of this solution is O(1)