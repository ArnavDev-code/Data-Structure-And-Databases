class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Strip trailing spaces and split by spaces
        words = s.strip().split()
        
        # Step 2: Return the length of the last element
        return len(words[-1]) if words else 0