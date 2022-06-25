class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        temp = []
        for i in toppingCosts:
            for j in range(2):
                temp.append(i)
        toppingCosts = temp[:]

        @functools.lru_cache(None)
        def recurse(cost,k1):
            diff = abs(cost-target)
            if diff not in dp:
                dp[diff] = []
                dp[diff].append(cost)
            else:
                dp[diff].append(cost)

            if k1 >= len(toppingCosts):
                return False

            for i in range(k1,len(toppingCosts)):
                y1 = recurse(cost+toppingCosts[i],i+1)

        minDiff = 10000000000000
        final_cost = 10000000000000
        for i in baseCosts:
            dp = {}
            recurse(i,0)
            list1 = list(dp.keys())
            if len(list1) == 0:
                continue
            ref = min(list1)
            x = min(dp[ref])
            if ref < minDiff:
                minDiff = ref
                final_cost = x
                continue
            if ref == minDiff:
                minDiff = ref
                if x < final_cost:
                    final_cost = x
                

        return(final_cost)
