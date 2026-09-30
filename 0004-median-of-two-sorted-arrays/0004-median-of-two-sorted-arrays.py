class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search time complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # Boundary conditions: edge values when partition is at the ends
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we found the correct partition point
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total elements count is odd
                if (m + n) % 2 == 1:
                    return float(max(maxLeftX, maxLeftY))
                # If total elements count is even (Fixed typo here)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
            elif maxLeftX > minRightY:
                # We are too far right in nums1, move left
                high = partitionX - 1
            else:
                # We are too far left in nums1, move right
                low = partitionX + 1
                
        raise ValueError("Input arrays are not sorted.")
