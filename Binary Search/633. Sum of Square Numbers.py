class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(0,40000):
            if c-i**2<=0:
                break
            if (c-i**2)**0.5 == int((c-i**2)**0.5):
                return True
        return False

