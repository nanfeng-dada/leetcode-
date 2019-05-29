# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
#  思路分析：当我们需要修剪root时，我们需要先修剪root->left、root->right，
#然后再修剪root。这显然是一个递归定义，所以采用递归法处理。
        if not root:
            return
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if root.val==0 and not root.left and not root.right:
            return
        return root