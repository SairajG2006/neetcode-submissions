class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left = n * [0]
        right = n * [0]
        l = 1
        r = 1

        for i, n in enumerate(nums):

            left[i] = l
            j = -i - 1
            right[j] = r
            l *= nums[i]
            r *= nums[j]
        
        return [l * r for l,r in zip(left,right)]