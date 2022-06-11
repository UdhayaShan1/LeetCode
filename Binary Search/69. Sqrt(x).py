class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        b1 = False
        start = 1
        end = 46340
        while b1==False:
            mid = (start+end) // 2
            if abs(start-end) <= 1:
                break
            if mid*mid > x:
                end = mid-1
                continue
            if mid*mid <= x:
                start = mid
                continue

        max1 = start
        if end*end <= x:
            max1 = end
        return(max1)
