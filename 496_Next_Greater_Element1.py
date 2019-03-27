class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, graph = [], {}
        res = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            graph[nums1[i]] = i
        
        for n in nums2:
            if not stack: stack.append(n)
            else:
                while stack and stack[-1] < n:
                    top = stack.pop()
                    if top in graph: res[graph[top]] = n
                stack.append(n)
        
        return res