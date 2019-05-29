# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 优化后的分治法
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        ld = self.getdepth(root.left)
        lr = self.getdepth(root.right)
        if ld == lr:
            # 最后一个节点在右子树
            return (1 << ld) + self.countNodes(root.right)
        else:
            return (1 << lr) + self.countNodes(root.left)

    def getdepth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth

# 分治暴力递归
class Solution1:
    def countNodes(self, root: TreeNode) -> int:
        return self.countNodes(root.left)+self.countNodes(root.right)+1 if root else 0