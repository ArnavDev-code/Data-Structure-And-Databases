class Solution:
    def intToRoman(self, num: int) -> str:
        # List of paired values and symbols ordered from largest to smallest
        roman_mapping = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100),  ("XC", 90),  ("L", 50),  ("XL", 40),
            ("X", 10),   ("IX", 9),   ("V", 5),   ("IV", 4),
            ("I", 1)
        ]
        
        result = []
        
        for symbol, value in roman_mapping:
            if num == 0:
                break
            # Find how many times the current value fits into the number
            count = num // value
            if count:
                result.append(symbol * count)
                num %= value  # Update num to the remainder
                
        return "".join(result)
