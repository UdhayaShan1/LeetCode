class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_one = []
        last_one = []
        
        for i in range(len(intervals)):
            x1 = intervals[i][0]
            y1 = intervals[i][1]
            x2 = newInterval[0]
            y2 = newInterval[1]
            if x2 >= x1 and y2 <= y1:
                start_one.append(i)
                continue
            if x2 >= x1 and x2 <= y1 and y2 >= y1:
                start_one.append(i)
                continue
            if x2 <= x1 and y2 >= y1:
                start_one.append(i)
                continue
            if x2 <= x1 and y2 <= y1 and y2 >= x1:
                start_one.append(i)
                continue

        print(start_one)
        if len(start_one) > 0:
            hash1 = {}
            for i in start_one:
                hash1[i] = 1
            min1 = min(intervals[start_one[0]][0],newInterval[0])
            max1 = max(intervals[start_one[-1]][-1],newInterval[-1])
            print([min1,max1])
            count = 0
            for i in range(len(intervals)):
                if i in hash1:
                    if i == start_one[0]:
                        intervals[i] = [min1,max1]
                    else:
                        intervals.pop(i-count)
                        count+=1
            return(intervals)
        else:
            last = -1
            first = -1
            for i in range(len(intervals)):
                x1 = intervals[i][0]
                y1 = intervals[i][1]
                if newInterval[0] >= x1:
                    first = i            
                if newInterval[-1] <= y1:
                    last = i
                    break
            print(first,last)
            if max(first,last) == -1:
                intervals.append(newInterval)
                return(intervals)
            else:
                if first >= 0:
                    intervals.insert(first+1,newInterval)
                    return(intervals)
                if last >= 0:
                    intervals.insert(last,newInterval)
                    return(intervals)
