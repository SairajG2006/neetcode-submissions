class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currMax = nums[0]
        currSum = 0

        for n in nums:

            if currSum < 0:
                currSum = 0

            currSum += n
            currMax = max(currMax, currSum)
        
        return currMax