class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #Base Case
        if(len(prices) == 1):
            return 0
        if(len(prices) == 2):
            if(prices[1] > prices[0]):
                return prices[1] - prices[0]
            else:
                return 0
        
        #General Case
        maxProfit = 0
        left = 0
        right = left + 1
        while(left < len(prices) and right < len(prices)):
            if(prices[left] <= prices[right]):
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
            elif(prices[left] > prices[right]):
                left = right
                right = left + 1
        return maxProfit

#The time complexity of this solution is O(n)
#The space complexity of this solution is O(n)