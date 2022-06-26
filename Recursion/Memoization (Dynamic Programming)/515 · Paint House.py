from typing import (
    List,
)

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here
        import sys
        dp = {}
        def dfs(k1,prev):
            if k1 >= len(costs):
                return 0
            
            if (k1,prev) in dp:
                return dp[(k1,prev)]
            
            
            if prev == -1:
                y1 = dfs(k1+1,"R")+costs[k1][0]
                y2 = dfs(k1+1,"B")+costs[k1][1]
                y3 = dfs(k1+1,"G")+costs[k1][2]
                dp[(k1,prev)] = min(y1,y2,y3)
            else:
                if prev == "R":
                    y1 = dfs(k1+1,"B")+costs[k1][1]
                    y2 = dfs(k1+1,"G")+costs[k1][2]
                    dp[(k1,prev)] = min(y1,y2)
                elif prev == "B":
                    y1 = dfs(k1+1,"R")+costs[k1][0]
                    y2 = dfs(k1+1,"G")+costs[k1][2]
                    dp[(k1,prev)] = min(y1,y2)
                else:
                    y1 = dfs(k1+1,"R")+costs[k1][0]
                    y2 = dfs(k1+1,"B")+costs[k1][1]
                    dp[(k1,prev)] = min(y1,y2)
            return dp[(k1,prev)]

        return(dfs(0,-1))
