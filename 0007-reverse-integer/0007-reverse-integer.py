class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Track the sign of the number
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits mathematically
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = (reversed_num * 10) + digit
            x //= 10
            
        # Reapply the sign
        reversed_num *= sign
        
        # Check for 32-bit signed integer overflow/underflow
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
            
        return reversed_num
