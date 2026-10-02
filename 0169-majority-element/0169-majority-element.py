class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elements = {}
        target = len(nums) // 2
        
        for num in nums:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1
                
            # Must be strictly greater than n // 2
            if elements[num] > target:
                return num
                
        # Fallback for single-element arrays like [1]
        return nums[0]
