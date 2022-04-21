class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp1 = {}
        for i in range(len(nums)):
            if nums[i] not in dp1:
                dp1[nums[i]] = 1
            else:
                dp1[nums[i]] += 1

        print(dp1)
        for i in nums:
            diff = target - i
            if diff == i:
                if diff in dp1:
                    if dp1[diff] > 1:
                        index = [j for j, x in enumerate(nums) if x == diff]
                        return([index[0],index[1]])
                        break
                else:
                    continue
            else:
                if diff in dp1:
                    return([[j for j, x in enumerate(nums) if x == i][0],[k for k, x in enumerate(nums) if x == diff][0]])
                    break
                else:
                    continue
