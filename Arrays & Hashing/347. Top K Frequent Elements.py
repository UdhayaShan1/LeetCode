class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for i in nums:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1


        count_list = list(dp.values())
        count_list.sort()
        dp1 = {k: v for k, v in sorted(dp.items(), key=lambda item: item[1])}

        count = 0
        list1 = []
        for i in range(len(dp1)-1,-1,-1):
            list1.append(list(dp1.keys())[i])
            count+=1
            if count == k:
                break

        return(list1)
