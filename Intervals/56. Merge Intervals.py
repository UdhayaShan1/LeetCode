class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i in range(len(intervals)-1):
            x1 = intervals[i][0]
            y1 = intervals[i][1]
            x2 = intervals[i+1][0]
            y2 = intervals[i+1][1]
            if x2 <= y1:
                new = [min(x1,x2),max(y1,y2)]
                intervals[i+1] = new
                intervals[i] = 0

        final = []
        for i in intervals:
            if i != 0:
                final.append(i)
        return(final)
