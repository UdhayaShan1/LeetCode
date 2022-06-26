class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        forward = {}
        backward = {}
        forward[0] = cardPoints[0]
        backward[0] = cardPoints[-1]
        for i in range(1,len(cardPoints)):
            forward[i] = cardPoints[i] + forward[i-1]


        for i in range(len(cardPoints)-2,-1,-1):
            backward[len(cardPoints)-i-1] = cardPoints[i]+backward[len(cardPoints)-i-2]


        import sys
        min1 = -sys.maxsize
        for i in range(0,k+1):
            if i == 0:
                if backward[k-1] > min1:
                    min1 = backward[k-1]
            elif i == k:
                if forward[i-1] > min1:
                    min1 = forward[i-1]
            else:
                sum1 = forward[i-1]+backward[k-i-1]
                if sum1 > min1:
                    min1 = sum1

        return(min1)
