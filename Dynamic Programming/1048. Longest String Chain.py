class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp_length = {}
        for i in words:
            dp_length[i] = len(i)

        dp2 = {k: v for k, v in sorted(dp_length.items(), key=lambda item: item[1])}

        final = []
        for i in list(dp2.keys()):
            final.append(i)

        words = final[:]

        def isPredecessor(word1, word2):
            if len(word1) + 1 != len(word2): return False
            i = 0
            for c in word2:
                if i == len(word1): return True
                if word1[i] == c:
                    i += 1
            return i == len(word1)


        dp = {}
        start = -1
        for i in range(len(words)):
            if len(words[i]) == len(words[0]):
                dp[i] = 1
            else:
                start = i
                break
        if start == -1:
            return 1
        for i in range(start,len(words)):
            min1 = 0
            for j in range(0,i):
                if isPredecessor(words[j],words[i]) == True:
                    if dp[j] >= min1:
                        min1 = dp[j]
            dp[i] = 1 + min1

        return(max(dp.values()))
