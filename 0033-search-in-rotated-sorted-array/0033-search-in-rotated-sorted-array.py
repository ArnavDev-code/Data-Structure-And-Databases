from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m] == target:
                return m

            # FIX 1: Check if the LEFT side is normally sorted
            elif nums[l] <= nums[m]:
                # If target is within this sorted left portion, launch inner search on it
                if nums[l] <= target < nums[m]:
                    r = m - 1
                    while l <= r:
                        b = (l+r) // 2
                        if nums[b] > target:
                            r = b - 1
                        elif nums[b] < target:
                            l = b + 1
                        else :
                            return b
                # Otherwise, target must be on the right side
                else:
                    l = m + 1
            
            # FIX 2: Otherwise, the RIGHT side must be normally sorted
            else:
                # If target is within this sorted right portion, launch inner search on it
                if nums[m] < target <= nums[r]:
                    l = m + 1
                    while l <= r:
                        a = (l+r) // 2
                        if nums[a] > target:
                            r = a - 1
                        elif nums[a] < target:
                            l = a + 1
                        else:
                            return a
                # Otherwise, target must be on the left side
                else:
                    r = m - 1

        return -1
