class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        visited  = [0 for _ in range(len(M))]
        for i in range(len(M)):
            if visited[i] == 0:
                count += 1
                queue = [i]
                while queue:
                    node = queue.pop(0)
                    visited[node] = 1
                    for j in range(len(M)):
                        if M[node][j] == 1 and visited[j] == 0:
                            queue.append(j)
        return count