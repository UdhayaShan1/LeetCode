import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        first = 1
        end = max(piles)

        b1 = False
        while b1==False:
            if abs(end-first) == 1:
                temp = [first,end]
                break
            middle = math.ceil((end+first)/2)
            count = 0
            for i in piles:
                count += math.ceil(i/middle)
            if count <= h:
                end = middle
            if count > h:
                first = middle

        temp.sort()
        for i in temp:
            count = 0
            for j in piles:
                count += math.ceil(j/i)
            if count <= h and count >= len(piles):
                return(i)
              
