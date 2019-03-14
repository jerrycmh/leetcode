class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        graph = set()
        ite = head
        while ite:
            if ite not in graph:
                graph.add(ite)
                ite = ite.next
            else:
                return ite
        return None