class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
                return True
        return False
            