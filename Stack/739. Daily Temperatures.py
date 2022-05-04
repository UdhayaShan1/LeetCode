class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max1 = max(temperatures[-1],temperatures[-2])
        dp = {}
        dp2 = {}
        dp[len(temperatures)-1] = 0
        dp2[len(temperatures)-1] = temperatures[-1]
        if temperatures[-2] < temperatures[-1]:
            dp[len(temperatures)-2] = 1
            dp2[len(temperatures)-2] = temperatures[-1]
        else:
            dp[len(temperatures)-2] = 0
            dp2[len(temperatures)-2] = temperatures[-2]

        for i in range(len(temperatures)-3,-1,-1):
            if temperatures[i] > max1:
                max1 = temperatures[i]
            if temperatures[i] >= max1:
                dp[i] = 0
                dp2[i] = temperatures[i]
                continue
            flag = 0
            if temperatures[i] < temperatures[i+1]:
                dp[i] = 1
                dp2[i] = temperatures[i+1]
                continue
            else:
                for j in range(i+1,len(temperatures)):
                    if temperatures[i] < temperatures[j]:
                        dp[i] = (j-i)
                        dp2[i] = temperatures[j]
                        flag+=1
                        break
                    if temperatures[i] < dp2[j]:
                        dp[i] = (j-i) + dp[j]
                        dp2[i] = dp2[j]
                        flag+=1
                        break
            if flag == 0:
                dp[i] = 0
                dp2[i] = temperatures[i]

        final = []
        for i in range(len(temperatures)):
            final.append(dp[i])
        return(final)
