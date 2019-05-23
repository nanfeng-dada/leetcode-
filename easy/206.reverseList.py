# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        s = []
        while head:
            s.append(head.val)
            head = head.next

        h = ListNode(None)
        h.next = ListNode(s.pop())
        cur = h.next
        while s:
            cur.next = ListNode(s.pop())
            cur = cur.next
        return h.next
class Solution1:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev