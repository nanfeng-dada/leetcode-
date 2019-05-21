# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 递归判断方法，写起来简单
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val==q.val and self.isSameTree(p.left,q.left) \
               and self.isSameTree(p.right, q.right)


# 采用队列，广度遍历
class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #         使用队列
        pl, ql = [p], [q]
        while pl and ql:
            a = pl.pop(0)
            b = ql.pop(0)

            if a == None and b == None:
                continue
            if a == None or b == None or a.val != b.val:
                return False

            pl.append(a.left)
            ql.append(b.left)
            pl.append(a.right)
            ql.append(b.right)
        return True