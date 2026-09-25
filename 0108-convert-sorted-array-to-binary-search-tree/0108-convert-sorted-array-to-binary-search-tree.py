# REMOVE OR COMMENT OUT THE 'class TreeNode:' BLOCK BEFORE SUBMITTING

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional['TreeNode']:
        def build_tree(left: int, right: int) -> Optional['TreeNode']:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid]) # LeetCode's built-in TreeNode is used here
            
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)
            
            return root
            
        return build_tree(0, len(nums) - 1)
