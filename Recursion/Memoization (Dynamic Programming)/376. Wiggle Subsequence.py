class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = {}
        def dfs(k,prev,flag):
            if k >= len(nums):
                return 0
            if (k,prev,flag) in dp:
                return dp[(k,prev,flag)]

            if k == 0:
                y1 = dfs(k+1,nums[k],1)+1
                y2 = dfs(k+1,nums[k],0)+1
                y3 = dfs(k+1,prev,flag)
                dp[(k,prev,flag)] = max(y1,y2,y3)
            else:
                if flag == 1:
                    if nums[k] > prev:
                        y1 = dfs(k+1,nums[k],0)+1
                        y2 = dfs(k+1,prev,flag)
                        dp[(k,prev,flag)] = max(y1,y2)
                    elif nums[k] <= prev:
                        y1 = dfs(k+1,prev,flag)
                        dp[(k,prev,flag)] = y1
                else:
                    if nums[k] < prev:
                        y1 = dfs(k+1,nums[k],1)+1
                        y2 = dfs(k+1,prev,flag)
                        dp[(k,prev,flag)] = max(y1,y2)
                    else:
                        y1 = dfs(k+1,prev,flag)
                        dp[(k,prev,flag)] = y1
            return dp[(k,prev,flag)]


        return(dfs(0,0,0))
