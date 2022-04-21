class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dp = {}
        for i in strs:
            str1 = list(i)
            str1.sort()
            str1 = ''.join(str1)
            if str1 not in dp:
                dp[str1] = []
                dp[str1].append(i)
            else:
                dp[str1].append(i)

        list1 = []
        for i in dp.values():
            list1.append(i)
        return(list1)
        
