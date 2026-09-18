class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Map to store the last seen index of each character
        max_length = 0
        left = 0       # Left boundary of the sliding window
        
        for right, char in enumerate(s):
            # If the character is already in the map and its index is inside 
            # our current window, move the left pointer past its last seen index
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update the character's last seen position
            char_map[char] = right
            
            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length
