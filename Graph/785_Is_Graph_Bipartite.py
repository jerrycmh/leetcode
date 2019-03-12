class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    n = stack.pop()
                    for neighbour in graph[n]:
                        if neighbour not in color:
                            if color[n] == 1: color[neighbour] = 0
                            else: color[neighbour] = 1
                            stack.append(neighbour)
                        elif color[neighbour] == color[n]:
                            return False
        
        return True