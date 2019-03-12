class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        
        for (begin, end), weight in zip(equations, values):
            if begin not in graph:
                graph[begin] = [(end, weight)]
            else:
                graph[begin].append((end, weight))
            if end not in graph:
                graph[end] = [(begin, 1/weight)]
            else:
                graph[end].append((begin, 1/weight))
        
        result = []
        for begin, end in queries:
            if begin not in graph or end not in graph:
                result.append(-1.0)
            else:
                queue = [(begin, 1.0)]
                visited = set()
                is_break = False
                while queue and not is_break:
                    node, value = queue.pop()
                    visited.add(node)
                    for next_n, v in graph[node]:
                        if next_n == end:
                            result.append(value*v)
                            is_break = True
                            break
                        else:
                            if next_n not in visited:
                                queue.append((next_n, value*v))
                if not is_break:
                    result.append(-1.0)
        
        return result