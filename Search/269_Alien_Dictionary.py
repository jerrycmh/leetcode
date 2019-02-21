class Solution:
    def alienOrder(self, words: 'List[str]') -> 'str':
        if not words:
            return ""
        
        level = {}
        graph = {}
        for word in words:
            for ch in word:
                if ch not in level: 
                    level[ch] = 0
                    graph[ch] = []
        
        for i in range(len(words)-1):
            for j in range(min(len(words[i]),len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    level[words[i+1][j]] += 1
                    if words[i][j] not in graph:
                        graph[words[i][j]] = [words[i+1][j]]
                    else:
                        graph[words[i][j]].append(words[i+1][j])
                    break
        
        queue, visited = [], []
        for key, value in level.items():
            if value == 0:
                queue.append(key)
                visited.append(key)
        
        result = ""
        while queue:
            ch = queue.pop(0)
            result += ch
            for child in graph[ch]:
                level[child] -= 1
                if level[child] == 0 and child not in visited:
                    queue.append(child)
                    visited.append(child)
        
        if len(result) != len(level.keys()):
            return ""
        else: return result