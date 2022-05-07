class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dp = {}
        dp3 = {}
        for i in arr:
            diff = abs(i-x)
            if diff not in dp:
                dp[diff] = []
                dp[diff].append(i)
            else:
                dp[diff].append(i)

        for i in dp:
            dp[i].sort()

        list1 = list(dp.keys())
        list1.sort()
        final = []
        for i in list1:
            final += dp[i]
            if len(final) >= k:
                break

        final = final[:k]
        final.sort()
        return final
