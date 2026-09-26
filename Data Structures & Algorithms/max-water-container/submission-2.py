class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        maxAmount = 0

        while left < right:

            amount = min(heights[left], heights[right]) * (right - left)
            maxAmount = max(maxAmount, amount)
            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return maxAmount