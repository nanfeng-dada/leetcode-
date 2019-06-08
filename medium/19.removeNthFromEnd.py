# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#方法1，一种两次遍历，依次求长度，第二次定位删除节点
# 方法2，一次遍历，两个节点操作，两个节点相隔n个节点，当后一个节点为空时
# 则第二个节点定位到删除的节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h=ListNode(None)
        h.next=head
        first=head
        second=head
        pre=h
        for _ in range(n):
            first=first.next
        while first:
            first=first.next
            pre=second
            second=second.next
        pre.next=second.next
        return h.next