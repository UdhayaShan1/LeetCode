class Solution:
    def maximumRemovals(self, s: str, p: str, removable1: List[int]) -> int:  
        import sys
        def isSub(m):
            i = j = 0
            remove = set(removable1[:m])
            while i < len(s) and j < len(p):
                if i in remove:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            return j == len(p)


        start = 0
        end = len(removable1)
        b1 = False
        while b1==False:
            middle = (start+end)//2
            if abs(start-end) <= 1:
                break

            x = isSub(middle)
            if x > 0:
                start = middle
                continue
            if x == 0:
                end = middle-1
                continue



        x = isSub(end)
        if x > 0:
            return end
        else:
            return start
    
    
