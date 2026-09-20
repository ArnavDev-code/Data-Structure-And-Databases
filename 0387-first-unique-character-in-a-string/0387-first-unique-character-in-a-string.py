class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}

        for letter in s:
            if letter in unique:
                unique[letter] += 1
            else:
                unique[letter] = 1

        for i in range(len(s)):
            if unique[s[i]] == 1:
                return i
        return -1