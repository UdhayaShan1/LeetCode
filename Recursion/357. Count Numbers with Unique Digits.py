class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        list1 = [0,1,2,3,4,5,6,7,8,9]
        ref_list = list1[:]
        dp = {}
        def dfs(length,ref_list):
            key = (length,tuple(ref_list))
            
            if length == n:
                return 1
            if length > n:
                return 0

            if key in dp:
                return dp[key]
            y1 = 0
            for i in range(len(ref_list)):
                if length == 0 and ref_list[i] == 0:
                    continue
                y1 += dfs(length+1,ref_list[:i]+ref_list[i+1:])
            dp[key] = y1
            return dp[key]

        sum1 = 0
        n1 = n
        for i in range(1,n1+1):
            n = i
            dp = {}
            sum1 += dfs(0,ref_list)
        return(sum1+1)
