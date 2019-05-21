# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#创建镜像子函数，递归调用该函数
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root, root)

    def ismirror(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return r1.val == r2.val and \
               self.ismirror(r1.right, r2.left) and self.ismirror(r2.right, r1.left)
# 采用队列，迭代
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        p=[root]
        q=[root]
        while q and p:
            r1=p.pop(0)
            r2=q.pop(0)
            if not r1 and not r2:
                continue
            if not r1 or not r2 or r1.val!=r2.val:
                return False
            p.append(r1.left)
            p.append(r1.right)
            q.append(r2.right)
            q.append(r2.left)
        return True