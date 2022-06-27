class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        start = 1
        end = 10**7

        import math
        b1 = False
        while b1==False:
            middle = (start+end)//2
            time = 0
            if abs(start-end) <= 1:
                break
            for i in range(len(dist)):
                if i != len(dist)-1:
                    time += math.ceil(dist[i]/middle)
                else:
                    time += (dist[i]/middle)
            if time > hour:
                start = middle+1
                continue
            if time <= hour:
                end = middle
                continue
                
        for k in [min(start,end),max(start,end)]:
            time = 0
            for i in range(len(dist)):
                if i != len(dist)-1:
                    time += math.ceil(dist[i]/k)
                else:
                    time += (dist[i]/k)
            if time <= hour:
                return k
        return -1
