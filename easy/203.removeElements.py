# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#注意cur与cur.next的区别,要删除节点一定要留有前驱
# 定义一个节点指向头结点，
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        h = ListNode(None)
        h.next = head
        cur = h
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return h.next
# 递归
class Solution1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next=self.removeElements(head.next,val)
        return head.next if head.val==val else head
