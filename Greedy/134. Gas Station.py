class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        final = []

        for i in range(len(gas)):
            final.append(gas[i]-cost[i])

        sum1 = sum(final)
        if sum1 >= 0:
            dp = {}
            flag = 0
            pos = 0
            if final[0] >= 0:
                flag = 1
                dp[0] = final[0]
                pos = 0
            else:
                flag = 0
                dp[0] = 0

            for i in range(1,len(final)):
                if flag == 0:
                    if final[i] >= 0:
                        flag+=1
                        dp[i] = final[i]
                        pos = i
                    else:
                        dp[i] = 0
                else:
                    dp[i] = final[i]
                    dp[i] += dp[i-1]
                    if dp[i] < 0:
                        dp[i] = 0
                        flag = 0
            return(pos)

        else:
            return(-1)
