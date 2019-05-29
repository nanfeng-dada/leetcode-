# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归翻转
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.helper(root.left)
        self.helper(root.right)
#递归翻转 ，精简
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        # 先翻转孩子节点，后翻转当前节点，这样在递归时，首先递归到最大深度，进行翻转，返回其父节点，接着翻转
        # 最后可以返回根节点
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
