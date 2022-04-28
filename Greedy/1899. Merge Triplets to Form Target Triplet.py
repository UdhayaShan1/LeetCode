class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag1 = 0
        flag2 = 0
        flag3 = 0
        for i in range(len(triplets)):
            a = triplets[i][0]
            b = triplets[i][1]
            c = triplets[i][2]
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                flag1+= 1
            if b == target[1]:
                flag2 += 1
            if c == target[2]:
                flag3 += 1

        if flag1 > 0 and flag2 > 0 and flag3 > 0:
            return(True)
        else:
            return(False)
