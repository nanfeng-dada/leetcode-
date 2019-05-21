# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归的方法，考虑每种情况
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if (not root.left) and (not root.right):
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
# 简化上述的代码,效率并没有提高
class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left or not right:
            return left + right + 1
        return min(left, right) + 1
# BFS，广度优先遍历
class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        q=[root]
        depth=0
        while(q):
            depth+=1
            for i in range(len(q)):
                cur=q.pop()
                # 为空，则为叶子节点
                if not cur:
                    break

                # cur不为none
                if cur:
                    q.append(cur.left)

                    q.append(cur.right)
        depth+=1

# 层次遍历
class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        depth = 0
        while (q):
            l = len(q)
            for i in range(l):
                cur = q.pop(0)
                # 左右孩子均为空，则为叶子节点，直接返回深度
                if (not cur.right) and (not cur.left):
                    return depth + 1

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)


