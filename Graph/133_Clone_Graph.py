class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        
        node_copy = UndirectedGraphNode(node.label)
        visited = {node: node_copy}
        queue = [node]
        
        while queue:
            cur = queue.pop(0)
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    neighbor_copy = UndirectedGraphNode(neighbor.label)
                    visited[cur].neighbors.append(neighbor_copy)
                    visited[neighbor] = neighbor_copy
                    queue.append(neighbor)
                else:
                    visited[cur].neighbors.append(visited[neighbor])
        
        return node_copy