class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Base Case
        if(len(height) == 2):
            return min(height[0], height[1])

        #General Case
        left = 0
        right = len(height) - 1
        max_area = -1
        while (left < right):
            max_area = max(min(height[left], height[right]) * (right - left), max_area)

            if(height[left] <= height[right]):
                left = left + 1
            else:
                right = right - 1
        return max_area

    #The time complexity of this solution is O(n)
    #The space complexity of this solution is O(1)