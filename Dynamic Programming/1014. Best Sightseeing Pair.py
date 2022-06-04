class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp1 = {}
        dp2 = {}
        list1 = []
        list2 = []
        for i in range(len(values)):
            list1.append(values[i]+i)
            list2.append(values[i]-i)

        dp1[0] = values[0]
        max1 = 0
        for i in range(1,len(list2)):
            if i == 1:
                if list2[i] + dp1[0] > max1:
                    max1 = list2[i] + dp1[0]
            else:
                dp1[i-1] = max(list1[i-1],dp1[i-2])
                if dp1[i-1] + list2[i] > max1:
                    max1 = dp1[i-1] + list2[i]

        return(max1)
