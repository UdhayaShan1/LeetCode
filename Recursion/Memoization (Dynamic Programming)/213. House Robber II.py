class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(first_taken,k1):
            if k1 >= len(nums):
                return 0

            if (first_taken,k1) in dp:
                return dp[(first_taken,k1)]

            if k1 == 0:
                y1 = dfs(True,k1+2)+nums[k1]
                y2 = dfs(False,k1+1)
                dp[(first_taken,k1)] = max(y1,y2)
            else:
                if k1 != len(nums)-1:
                    y1 = dfs(first_taken,k1+2)+nums[k1]
                    y2 = dfs(first_taken,k1+1)
                    dp[(first_taken,k1)] = max(y1,y2)
                else:
                    if first_taken == True:
                        y1 = dfs(first_taken,k1+1)
                        dp[(first_taken,k1)] = y1
                    else:
                        y1 = dfs(first_taken,k1+1)
                        y2 = dfs(first_taken,k1+2)+nums[k1]
                        dp[(first_taken,k1)] = max(y1,y2)

            return dp[(first_taken,k1)]

        return(dfs(True,0))
