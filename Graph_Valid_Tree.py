class Solution:
    def validTree(self, n: 'int', edges: 'List[List[int]]') -> 'bool':
        if not edges:
            if n == 1:
                return True
            else:
                return False
        
        node = [i for i in range(n)]
        if len(edges) != n-1:
            return False
        
        for n1, n2 in edges:
            #find n1 parent
            while n1 != node[n1]:
                n1 = node[n1]
            #find n2 parent:
            while n2 != node[n2]:
                n2 = node[n2]
            
            #If they belong to one subset, then there is a cycle
            if n1 == n2:
                return False
            #Set n2's parent as n1, now they are in one subset of n1
            node[n2] = n1
            
        return True