class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l , r  = 0 , len(nums) - 1
        first = -1
        second = -1

        #first occurance
        while l <= r:
            m = (l+ r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                r = m - 1
                first = m
            else:
                r = m - 1
       
        #last occurance
        l , r  = 0 , len(nums) - 1

        while l <= r:
            m = (l+ r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                second = m
                l = m + 1
            else:
                r = m - 1

        return [first , second]