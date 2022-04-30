class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dp = {}
        for i in s:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1

        temp = []
        final_length = []

        b1 = False
        start = 0
        while b1==False:
            temp.append(s[start])
            dp[s[start]] -= 1
            flag = 0
            for i in temp:
                if dp[i] > 0:
                    flag+=1
                    break
            if flag > 0:
                start += 1
            else:
                final_length.append(len(temp))
                temp = []
                start += 1
            if start == len(s):
                break

        return final_length
