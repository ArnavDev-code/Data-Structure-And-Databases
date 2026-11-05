class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine if the final result should be negative
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        # Perform bitwise division
        while a >= b:
            temp_divisor = b
            multiple = 1
            # Double the divisor until it exceeds the remaining dividend
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest doubled divisor found
            a -= temp_divisor
            quotient += multiple
            
        # Apply the sign and ensure the result stays within 32-bit bounds
        result = -quotient if negative else quotient
        return max(INT_MIN, min(INT_MAX, result))
