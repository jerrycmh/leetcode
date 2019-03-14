# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getNum(self, node):
        num = 0
        while node:
            num = num*10 + node.val
            node = node.next
        return num
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0: return l2
        if l2.val == 0: return l1
        
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        
        s = num1+num2
        
        head = ListNode(0)
        ite = head
        stack = []
        while s:
            stack.append(s%10)
            s = s//10
        while stack:
            ite.next = ListNode(stack.pop())
            ite = ite.next
        return head.next