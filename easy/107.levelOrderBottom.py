# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#层次遍历，并返回每层数据
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []

        ceng_all = []
        p = [root]
        while p:
            l = len(p)
            ceng = []
            for i in range(l):

                if p[0].val != None:
                    ceng.append(p[0].val)
                if p[0].left:
                    p.append(p[0].left)
                if p[0].right:
                    p.append(p[0].right)

                p.pop(0)
            ceng_all.append(ceng)
        return ceng_all[::-1]



