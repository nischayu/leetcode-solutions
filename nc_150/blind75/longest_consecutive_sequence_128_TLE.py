class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Base Case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        #Note: Set is implemented as a hash table in Python
        #So LOOKUP times in set is O(1)
        nums_set = set(nums)
        max_length = 1

        #General Case
        for i in range(0, len(nums)):
            curr_len = 1
            ptr = nums[i] - 1

            #Left of nums[i]
            while(True): 
                if(ptr in nums_set):
                    curr_len+=1
                    ptr -= 1
                else:
                    break
            while(True):
                if(ptr in nums_set):
                    curr_len +=1
                    ptr += 1
                else:
                    break
            if(curr_len > max_length):
                max_length = curr_len

        return max_length

#The space complexity of this solution is O(1)
#The time complexity of this solution is O(n^2) because for each
#num[i] we still scan the rest of the array in it's entirety