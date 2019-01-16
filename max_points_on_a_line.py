class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        lines = {}
        sorted_points = sorted((p for p in points), key=lambda a: a.x)
        for i in range(len(sorted_points) - 1):
            for j in range(i + 1, len(sorted_points)):
                if (sorted_points[j].x - sorted_points[i].x) != 0:
                    # save 4 decimal points
                    line_a = int( 10000 * (sorted_points[j].y - sorted_points[i].y) / (sorted_points[j].x - sorted_points[i].x))
                    line_b = 10000 * sorted_points[j].y - (line_a) * sorted_points[j].x
                else:
                    line_a = 'inf'
                    line_b = sorted_points[j].x
                if (line_a, line_b) not in lines:
                    lines[(line_a, line_b)] = set()                
                lines[(line_a, line_b)].add(sorted_points[j])
                lines[(line_a, line_b)].add(sorted_points[i])
        
        return 0 if len(points) == 0 else 1 if len(points) == 1 else max(len(list(v)) for v in lines.values())