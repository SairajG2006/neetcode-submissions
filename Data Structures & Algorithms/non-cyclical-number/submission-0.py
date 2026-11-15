class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        
        return False
    
    def sumOfSquares(self, n: int) -> int:

        total = 0
        while n > 0:
            total += (n % 10) * (n % 10)
            n //= 10
        return total
    
    
        