class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = {}

        for i in range(0, len(nums)):
            if(target - nums[i] in mapping):
                return [mapping[target-nums[i]], i]
            else:
                mapping[nums[i]] = i
        return False

#The time complexity of this solution is O(n)
#The space complexity of this solution is O(n)