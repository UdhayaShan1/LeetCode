class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dp = {}
        for i in range(len(arr)):
            if arr[i] not in dp:
                dp[arr[i]] = []
                dp[arr[i]].append(i)
            else:
                dp[arr[i]].append(i)
        
        for i in arr:
            ref = i * 2
            if ref != i:
                if ref in dp:
                    return True
            else:
                if len(dp[ref]) > 1:
                    return True
        
        return False
