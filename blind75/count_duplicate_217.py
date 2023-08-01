class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}

        for num in nums:
            if num in mapping:
                return True
            else:
                mapping[num] = None
        return False

#The time complexity of this solution is O(n) where 
# n is the number of items in nums. "if nums in mapping" 
# takes O(1) time to lookup
#The space complexity of this solution is O(n)