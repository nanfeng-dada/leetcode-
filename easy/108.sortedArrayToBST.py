# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 分治法
class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None
        # 这两句等价
        # mid = len(nums) // 2
        mid = len(nums) >> 1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root