class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize == 0:
            set_list = list(set(hand))
            set_list.sort()
            dp = {}
            for i in hand:
                if i not in dp:
                    dp[i] = 1
                else:
                    dp[i] += 1
            flag = 0

            for i in range(len(set_list)):
                if i+groupSize > len(set_list):
                    break
                multi = dp[set_list[i]]
                if multi == 0:
                    continue
                for j in range(set_list[i],set_list[i]+groupSize):
                    if j not in dp:
                        flag+=2
                        return False
                    dp[j] -= multi
                    if dp[j] < 0:
                        flag+=1
                        return False
                if flag == 1 :
                    break
                if flag == 2:
                    break
            for i in dp.values():
                if i > 0:
                    return False
            return True
        else:
            return False
          
