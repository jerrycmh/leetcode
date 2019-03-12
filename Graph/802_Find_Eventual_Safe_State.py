class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = [False for _ in range(len(graph))]
        g, queue = {}, []
        for i, nodes in enumerate(graph):
            if not nodes: 
                queue.append(i)
            else: g[i] = nodes
        
        while queue:
            node = queue.pop(0)
            safe[node] = True
            for key, val in g.items():
                if node in val:
                    g[key].remove(node)
                    if not g[key]: 
                        queue.append(key)
        
        return [i for i, x in enumerate(safe) if x]