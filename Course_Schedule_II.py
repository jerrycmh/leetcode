class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result = []
        graph = {}
        
        for post, pre in prerequisites:
            if pre not in graph:
                graph[pre] = [post]
            else:
                graph[pre].append(post)
        
        post_stack = [i for i in range(numCourses) if i not in graph]
        
        while post_stack:
            course = post_stack.pop()
            for key, value in graph.items():
                if course in value:
                    value.remove(course)
                    if len(value) == 0:
                        post_stack.append(key)
            result.append(course)
        
        if len(result) != numCourses:
            return []
        else:
            return result[::-1]