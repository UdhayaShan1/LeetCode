class Solution:
    def maxProfit(self, list1: List[int]) -> int:
        min1 = 100000000
        max1 = 0
        if list1[0] < min1:
            min1 = list1[0]

        for i in range(1,len(list1)):
            if list1[i] > min1:
                if list1[i] - min1 > max1:
                    max1 = list1[i] - min1
            else:
                min1 = list1[i]

        return(max1)
