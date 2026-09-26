class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        left = 0
        result = 0

        for i in range(len(s)):

            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[i])
            result = max(result, i - left + 1)
        
        return result
            
