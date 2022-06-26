class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def num_ways(self, n: int, k: int) -> int:
        # write your code here
        nums = []
        for i in range(1,k+1):
            nums.append(i)

        import sys
        dp = {}

        def dfs(length,two_adjacent,prev):
            if length == n:
                return 1
            if length > n:
                return 0
            
            if (length,two_adjacent,prev) in dp:
                return dp[(length,two_adjacent,prev)]
            
            
            y1 = 0
            for i in range(len(nums)):
                if prev == -1:
                    y1 += dfs(length+1,two_adjacent,nums[i])
                else:
                    if two_adjacent == False:
                        if nums[i] == prev:
                            y1 += dfs(length+1,True,nums[i])
                        else:
                            y1 += dfs(length+1,two_adjacent,nums[i])
                    else:
                        if nums[i] == prev:
                            continue
                        else:
                            y1 += dfs(length+1,False,nums[i])
            dp[(length,two_adjacent,prev)] = y1
            return y1
            
            
        return(dfs(0,False,-1))
