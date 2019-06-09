# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#自己写的
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #         处理空链表
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1
        #         初始化两个节点，一个用于返回的头结点，一个指向头结点用于滑动
        #           赋值的当前节点
        h = ListNode(None)
        cur = h
        flag = 0
        while l1 and l2:
            cur.next = ListNode((l1.val + l2.val + flag) % 10)

            flag = (l1.val + l2.val + flag) // 10

            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            cur.next = ListNode((l1.val + flag) % 10)
            flag = (l1.val + flag) // 10
            cur = cur.next
            l1 = l1.next
        while l2:
            cur.next = ListNode((l2.val + flag) % 10)
            flag = (l2.val + flag) // 10
            cur = cur.next
            l2 = l2.next
        if flag:
            cur.next = ListNode(1)

        return h.next

# 大佬写的，将空值置为0，很好的处理了特殊情况
class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next