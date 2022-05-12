class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        part = []
        def paran(left,right):
            if left == right and left == n:
               res.append(''.join(part.copy()))
               return True
            if left > n:
                return False
            if right > n:
                return False
            if left + right > 2*n:
                return False

            if left < n:
                part.append("(")
                paran(left+1,right)
                part.pop()
            if right < left and right < n:
                part.append(")")
                paran(left,right+1)
                part.pop()

        paran(0,0)
        return(res)
