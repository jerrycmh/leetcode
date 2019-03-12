class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        stack = [(sr, sc)]
        visited = []
        while stack:
            x, y = stack.pop()
            if (x, y) not in visited and image[x][y] == oldColor:
                image[x][y] = newColor
                if x-1 >= 0 and image[x-1][y] == oldColor:
                    stack.append((x-1, y))
                if y-1 >= 0 and image[x][y-1] == oldColor:
                    stack.append((x, y-1))
                if x+1 < len(image) and image[x+1][y] == oldColor:
                    stack.append((x+1, y))
                if y+1 < len(image[0]) and image[x][y+1] == oldColor:
                    stack.append((x, y+1))
                visited.append((x, y))
        return image