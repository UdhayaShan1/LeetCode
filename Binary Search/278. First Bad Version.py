# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# def isBadVersion(num1) - own helper function for IDE:
    #if num1 >= bad:
    #    return True
    #else:
    #   return False



class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        last = n

        b1 = False
        while b1==False:
            if abs(start-last) <= 1:
                break
            mid = (start+last)//2
            if isBadVersion(mid) == False:
                start = mid+1
                continue
            if isBadVersion(mid) == True:
                last = mid
        if isBadVersion(start) == True:
            return start
        if isBadVersion(last) == True:
            return last
