# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归，写起来比较简单
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        # +1操作放在外面能将程序效率提高
        # return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

#层次遍历获取深度
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
    # 使用队列,广度优先遍历,遍历一层,深度加1
        if not root:
            return 0
        p=[root]
        depth=0
        while p:
            depth+=1
            # 处理当前层
            for i in range(len(p)):
                if p[0].left:
                    p.append(p[0].left)
                if p[0].right:
                    p.append(p[0].right)
                # 处理完一个节点，弹出
                p.pop(0)
        return depth

#使用堆栈，深度优先遍历，获取深度，遍历过程中实时更新最大深度
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 堆栈里保存节点以及节点的深度信息
        p=[(1,root)]
        depth=0
        while p:
            curdepth,r=p.pop()
            depth=max(depth,curdepth)
            if r.left:
                p.append((curdepth+1,r.left))
            if r.right:
                p.append((curdepth+1,r.right))
        return depth



