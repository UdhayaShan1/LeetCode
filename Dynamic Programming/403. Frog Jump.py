class Solution:
    def canCross(self, stones: List[int]) -> bool:
        #stones = [0,1,3,5,6,8,12,17]
        stonesdp = {}
        for i in stones:
            stonesdp[i] = 1


        dp = {}
        dp2 = {}
        def recurse(pos,prev):
            #print(pos,prev)
            if pos not in stonesdp:
                return 0
            if pos == stones[-1]:
                return 1
            key = (pos,prev)
            if key in dp:
                return dp[key]

            if prev == -1:
                for2 = recurse(pos+1,1)
                dp[key] = for2
            else:
                if prev == 1:
                    for2 = recurse(pos+(prev),prev)
                    for3 = recurse(pos+(prev+1),prev+1)
                    dp[key] = for2+for3
                else:
                    for1 = recurse(pos+(prev-1),prev-1)
                    for2 = recurse(pos+(prev),prev)
                    for3 = recurse(pos+(prev+1),prev+1)
                    dp[key] = for1+for2+for3
            return dp[key]

        return(recurse(0,-1))>0
