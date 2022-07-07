class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        import sys
        dp = {}
        def dfs(cards):
            if len(cards) == 1:
                if abs(cards[0] - 24) <= 0.1:
                    return 1
                else:
                    return 0

            y1 = 0
            for i in range(len(cards)):
                for j in range(len(cards)):
                    if i == j:
                        continue
                    cards2 = cards[:]
                    sum1 = cards[i]+cards[j]
                    cards2.remove(cards[i])
                    cards2.remove(cards[j])
                    cards2.append(sum1)
                    y1 += dfs(cards2)

                    cards2 = cards[:]
                    sub1 = cards[i]-cards[j]
                    cards2.remove(cards[i])
                    cards2.remove(cards[j])
                    cards2.append(sub1)
                    y1 += dfs(cards2)

                    cards2 = cards[:]
                    prod1 = cards[i]*cards[j]
                    cards2.remove(cards[i])
                    cards2.remove(cards[j])
                    cards2.append(prod1)
                    y1 += dfs(cards2)

                    if cards[j] != 0:
                        cards2 = cards[:]
                        div1 = cards[i]/cards[j]
                        cards2.remove(cards[i])
                        cards2.remove(cards[j])
                        cards2.append(div1)
                        y1 += dfs(cards2)
            return y1


        return(dfs(cards)>=1)
