class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dp = {}
        dp2 = {}

        for i in range(len(position)):
            dp[position[i]] = speed[i]
            dp2[position[i]] = (target-position[i]) / speed[i]

        position.sort()
        position = position[::-1]

        for i in range(len(position)-1):
            if dp2[position[i]] >= dp2[position[i+1]]:
                dp2[position[i+1]] = dp2[position[i]]

        return(len(set(list(dp2.values()))))
