class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums) #using set, lookup takes O(1) time

        for i in range(0, len(nums)):
            is_consecutive = True
            if(nums[i]-1 in nums_set): #not the start of a sequence
                continue
            else:
                curr_length = 1
                curr = nums[i] + 1
                while(is_consecutive):
                    if(curr in nums_set):
                        curr_length += 1
                        curr += 1
                    else:
                        is_consecutive = False
                max_length = max(max_length, curr_length)
        return max_length

    #The time complexity of this solution is O(n)
    #The space complexity of this solution is O(n)