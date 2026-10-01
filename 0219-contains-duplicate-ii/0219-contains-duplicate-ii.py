class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        position = {}

        for i in range(len(nums)):
            if nums[i] in position:
                if i - position[nums[i]] <= k:
                    return True
            position[nums[i]] = i
        return False
                