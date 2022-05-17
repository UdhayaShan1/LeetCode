class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = str(digits)
        dp = {}
        dp[2] = "abc"
        dp[3] = "def"
        dp[4] = "ghi"
        dp[5] = "jkl"
        dp[6] = "mno"
        dp[7] = "pqrs"
        dp[8] = "tuv"
        dp[9] = "wxyz"

        res = []
        def recurse(arr,k):
            if len(arr) == len(digits):
                res.append(''.join(arr.copy()))
                return True
            if len(arr) > len(digits):
                return False

            for i in range(k,len(digits)):
                for j in dp[int(digits[i])]:
                    arr.append(j)
                    recurse(arr,i+1)
                    arr.pop()

        recurse([],0)
        if len(res) == 1:
            return []
        return(res)
