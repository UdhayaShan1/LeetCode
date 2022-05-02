class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = (sum(nums)/2)
        if int(target) != target:
            return False
        target = int(target)
        dp_count = {}
        for i in nums:
            if i not in dp_count:
                dp_count[i] = 1
            else:
                dp_count[i] += 1

        nums.sort()
        dp = {}
        dp_index = {}
        print(nums)
        for i in range(1,target+1):
            dp[i] = False
            if i < nums[0]:
                dp[i] = False
                dp_index[i] = {}
                continue
            else:
                for j in nums:
                    if i == j:
                        dp[i] = True
                        dp_index[i] = {}
                        dp_index[i][j] = 1
                        break
                    if i > j:
                        remainder = i - j
                        if dp[remainder] == False:
                            continue
                        if j not in dp_index[remainder]:
                            dp[i] = True
                            dp_index[i] = dp_index[remainder].copy()
                            dp_index[i][j] = 1
                            break
                        else:
                            if dp_index[remainder][j] + 1 <= dp_count[j]:
                                dp[i] = True
                                dp_index[i] = dp_index[remainder].copy()
                                dp_index[i][j] += 1
                                break

        return dp[target]
