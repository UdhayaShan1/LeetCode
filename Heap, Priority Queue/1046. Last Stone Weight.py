class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        b1 = False
        while b1==False:
            if len(stones) <=1:
                break
            stones.sort()
            if stones[-2] == stones[-1]:
                stones.pop(-1)
                stones.pop(-1)
                continue
            if stones[-1] > stones[-2]:
                temp = stones[-1] - stones[-2]
                stones.pop(-1)
                stones.pop(-1)
                stones.append(temp)
                continue
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
