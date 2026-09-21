class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Start from the last digit and move backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it rolls over to 0
            digits[i] = 0
            
        # If all digits were 9 (e.g., [9, 9, 9] became [0, 0, 0]), 
        # we insert a 1 at the beginning to make it 1000
        return [1] + digits
