# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#第一种方式，使用栈
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = self.getlen(head)
        if l <= 1:
            return True
        # print(l)
        stack = []
        cnt = 0
        while cnt < l >> 1:
            cnt += 1
            stack.append(head.val)
            # print(stack)
            head = head.next

        if l % 2:
            head = head.next
        while head:
            if stack.pop() != head.val:
                return False
            head = head.next
        return True

    def getlen(self, h):
        l = 0
        while h:
            l += 1
            h = h.next
        return l

# 翻转后半部分链表，再依次对比每个位置上的值

class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        l = self.getlen(head)
        if l <= 1:
            return True
        cnt=0
        pre,cur=None,head
        while cnt<l>>1:
            cnt+=1
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        if l%2:
            cur=cur.next
        while cur:
            if cur.val!=pre.val:
                return False
            cur=cur.next
            pre=pre.next
        return True

    def getlen(self, h):
        l = 0
        while h:
            l += 1
            h = h.next
        return l