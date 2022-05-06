class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        max1 = 10000000000
        index = -1
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            if x1 == x or y1 == y:
                if abs(x1 - x) + abs(y1 - y) < max1:
                    max1 = abs(x1 - x) + abs(y1 - y)
                    index = i
        return(index)
