class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        dp = {}
        for i in arr:
            dp[i] = 1
        list1 = []
        for i in range(1,500000000000000000):
            if i not in dp:
                list1.append(i)
            if len(list1) >= k:
                break

        if k >= len(list1):
            return list1[-1]
        else:
            return list1[k-1]
