class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        import sys
        dp = {}
        def dfs(amount,needs,k1):
            if k1 >= len(special):
                count = 0
                for i in range(len(needs)):
                    count += needs[i]*price[i]
                return amount+count

            if (amount,tuple(needs),k1) in dp:
                return dp[(amount,tuple(needs),k1)]



            y1 = dfs(amount,needs,k1+1)
            dp[(amount,tuple(needs),k1)] = y1
            ref = special[k1][:-1]
            need2 = needs.copy()
            flag = 0
            for i in range(len(ref)):
                if need2[i] < ref[i]:
                    flag+=1
                    break
                need2[i] -= ref[i]
            if flag >= 1:
                y1 = dfs(amount,needs,k1+1)
                dp[(amount,tuple(needs),k1)] = y1
            else:
                y1 = dfs(amount,needs,k1+1)
                y2 = dfs(amount+special[k1][-1],need2,k1)
                dp[(amount,tuple(needs),k1)] = min(y1,y2)
            return dp[(amount,tuple(needs),k1)]

        return(dfs(0,needs,0))
        
