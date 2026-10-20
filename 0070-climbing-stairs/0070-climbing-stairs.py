class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Base cases for n = 1 and n = 2
        prev2 = 1  # ways(1)
        prev1 = 2  # ways(2)
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1
