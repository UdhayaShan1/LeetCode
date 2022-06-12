class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        set1 = list(set(nums))
        dp_count = {}
        for i in nums:
            if i not in dp_count:
                dp_count[i]=1
            else:
                dp_count[i]+=1

        dp = {}
        def dfs(k):
            if k >= len(set1):
                return 0
            if k in dp:
                return dp[k]

            if k < len(set1)-1:
                if set1[k+1] - set1[k] > 1:
                    include = dfs(k+1) + dp_count[set1[k]]*set1[k]
                    exclude = dfs(k+1)
                    dp[k] = max(include,exclude)
                else:
                    include = dfs(k+2) + dp_count[set1[k]]*set1[k]
                    exclude = dfs(k+1)
                    dp[k] = max(include,exclude)
            else:
                include = dfs(k+1) + dp_count[set1[k]]*set1[k]
                exclude = dfs(k+1)
                dp[k] = max(include,exclude)

            return dp[k]

        return(dfs(0))
