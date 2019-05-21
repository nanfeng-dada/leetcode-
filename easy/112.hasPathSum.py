# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#采用堆栈进行DFS，求解所有路径和，最后判断指定和是否在
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        q = [(root.val, root)]
        allsum = []
        while q:
            cursum, node = q.pop()

            if not node.right and not node.left:
                allsum.append(cursum)
            if node.left:
                q.append((cursum + node.left.val, node.left))
            if node.right:
                q.append((cursum + node.right.val, node.right))
        return sum in allsum
# 采用递归,递归返回值一般可通过and or max min 等去构造
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum==root.val
        else:
            return self.hasPathSum(root.right,sum-root.val) or \
                   self.hasPathSum(root.left,sum-root.val)
