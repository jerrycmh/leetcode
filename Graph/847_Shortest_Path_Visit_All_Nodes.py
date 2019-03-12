class Solution:
	def shortestPathLength(self, graph):
		node_count = len(graph)
		masks = [1 << i for i in range(node_count)]
		all_visited = (1 << node_count) - 1
		queue = [(i, masks[i]) for i in range(node_count)]
		visited = [{masks[i]} for i in range(node_count)]
		steps = 0

		while queue:
			size = len(queue)
			while size:
				cur, state = queue.pop(0)
				if state == all_visited:
					return steps
				for node in graph[cur]:
					new_state = state | masks[node]
					if new_state == all_visited:
						return steps+1
					if new_state not in visited[node]:
						visited[node].add(new_state)
						queue.append((node, new_state))
				size -= 1
			steps += 1

		return float('inf')