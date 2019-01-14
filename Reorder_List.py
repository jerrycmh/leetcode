# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        ite = begin = head
        real_end = head.next
        while ite:
            if ite.next == None:
                end = ite
            elif ite.next.next == None:
                prev_end = ite
            ite = ite.next
        
        while real_end and real_end.next:
            begin.next = end
            end.next = real_end
            prev_end.next = None
            
            begin = real_end
            real_end = real_end.next
            ite = begin.next
            while ite:
                if ite.next == None:
                    end = ite
                elif ite.next.next == None:
                    prev_end = ite

                ite = ite.next

    def reorderList2(self, head):
        if not head:
            return None
        
        nodeList = []
        node = head
        
        while node:
            nodeList.append(node)
            node = node.next
        
        l, r = 0, len(nodeList) - 1
        
        while l < r:
            nodeList[l].next = nodeList[r]
            nodeList[r].next = nodeList[(l + 1)]
            l += 1; r -= 1
        
        nodeList[l].next = None