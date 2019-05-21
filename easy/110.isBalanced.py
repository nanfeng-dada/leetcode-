# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归判断左右孩子是否都是，平衡的
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        #         空节点，为平衡
        if not root:
            return True
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    # 104题获取数的最大深度
    def get_height(self, r):
        if not r:
            return 0
        return max(self.get_height(r.left), self.get_height(r.right)) + 1
# 上面这种Brute Froce的方法，整棵树有很多冗余无意义的遍历，其实我们在处理完get_height这个高度的时候，
# 我们完全可以在检查每个节点高度并且返回的同时，记录左右差是否已经超过1，
# 只要有一个节点超过1，那么直接返回False即可
class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        #         空节点，为平衡
        self.balance = True
        self.get_height(root)
        return self.balance
    # 104题获取数的最大深度
    def get_height(self, r):
        if not r:
            return 0
        left=self.get_height(r.left)
        right=self.get_height(r.right)
        if abs(left-right)>1:
            self.balance=False
        return max(left,right ) + 1
# 在上述代码中加入self.balance标志，作为判定结果，但是高度数据并没有使用
# 可以将非平衡的高度数据置为-1，作为标志返回，省去原标志
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:

        height=self.get_height(root)
        return height!=-1
    # 104题获取数的最大深度
    def get_height(self, r):
        if not r:
            return 0

        left=self.get_height(r.left)
        right=self.get_height(r.right)
        # 如果此时就出现左右有非平衡数的情况
        if left==-1 or right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return max(left,right ) + 1