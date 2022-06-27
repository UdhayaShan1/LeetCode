class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start = k
        end = sum(candies)
        b1 = False
        while b1==False:
            middle = (start+end)//2
            each = middle//k
            if each == 0:
                break
            if abs(start-end) <= 1:
                break
            count = 0
            for i in candies:
                if i >= each:
                    count+=(i//each)
            if count >= k:
                start = middle
                continue
            if count < k:
                end = middle-1
                continue
        
        if each == 0:
            return 0
        
        for i in range(end+10,start-10,-1):
            if i == 0:
                break
            each = i // k
            count = 0
            for j in candies:
                if j >= each:
                    count += j//each
            if count >= k:
                return i//k
        return 0
