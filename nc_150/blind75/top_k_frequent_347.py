class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Base Case
        if(len(nums) == 1):
            return nums

        #General Case
        val_to_freq = {}
        buckets = [[] for i in range(0, len(nums) + 1)]

        for num in nums:
            val_to_freq[num] = 1 + val_to_freq.get(num, 0)

        for val, freq in val_to_freq.items():
            buckets[freq].append(val)
        
        result = []
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                result.append(j)
                if(len(result) == k):
                    return result
        return False 

    #The time complexity of this solution is O(n)
    #The space complexity of this solution is O(n)