class Solution:
    def mincostTickets(self, days1: List[int], costs: List[int]) -> int:
        dp = {}
        def dfs(k1,days):
            if k1 >= len(days1):
                return 0

            if (k1,days) in dp:
                return dp[(k1,days)]

            if days1[k1] < days:
                y1 = dfs(k1+1,days)
                dp[(k1,days)] = y1
            else:
                y1 = dfs(k1+1,days1[k1]+1)+costs[0]
                y2 = dfs(k1+1,days1[k1]+7)+costs[1]
                y3 = dfs(k1+1,days1[k1]+30)+costs[2]
                dp[(k1,days)] = min(y1,y2,y3)

            return dp[(k1,days)]

        return(dfs(0,days1[0]))
