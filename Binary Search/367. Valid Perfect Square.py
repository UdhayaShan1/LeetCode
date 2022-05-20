class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,50000):
            if i**2 > num:
                return False
            if i**2 == num:
                return True
        
        return False
        
