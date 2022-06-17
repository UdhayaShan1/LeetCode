class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        import sys
        dp = {}
        def dfs(i,j):
            if i >= len(triangle):
                return 0
            if j >= len(triangle) or j < 0:
                if i >= len(triangle):
                    return 0
                else:
                    return sys.maxsize

            if (i,j) in dp:
                return dp[(i,j)]


            y1 = dfs(i+1,j)+triangle[i][j]
            y2 = dfs(i+1,j+1)+triangle[i][j]
            dp[(i,j)] = min(y1,y2)
            return dp[(i,j)]

        return(dfs(0,0))
