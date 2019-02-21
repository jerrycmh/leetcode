class Solution:
    def cutOffTree(self, forest: 'List[List[int]]') -> 'int':
        trees = [(v, row, col) for row, lists in enumerate(forest) for col, v in enumerate(lists) if v>1]
        trees = sorted(trees)
        
        start_r = start_c = res = 0
        for v, target_r, target_c in trees:
            d = self.bfs(forest, start_r, start_c, target_r, target_c)
            if d < 0: return -1
            res += d
            start_r, start_c = target_r, target_c
        return res

    def bfs(self,forest, sr, sc, tr, tc):
        visited = {(sr, sc)}
        queue = [(sr, sc, 0)]
        while queue:
            row, col, depth = queue.pop(0)
            if row == tr and col == tc: return depth
            else:
                for next_r, next_c in [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]:
                    if 0<=next_r and next_r<len(forest) and 0<=next_c and next_c<len(forest[0]) and (next_r, next_c) not in visited and forest[next_r][next_c] != 0:
                        visited.add((next_r, next_c))
                        queue.append((next_r, next_c, depth+1))
        return -1