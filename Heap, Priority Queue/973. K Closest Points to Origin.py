class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dp = {}
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            dp[i] = ((x1)**2 + (y1)**2)**0.5

        dp2 = {k: v for k, v in sorted(dp.items(), key=lambda item: item[1])}
        print(dp2)
        count = 0
        final = []
        for i in dp2:
            final.append(points[i])
            count+=1
            if count == k:
                break

        return(final)
