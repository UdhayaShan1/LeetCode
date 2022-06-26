class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def can_permute_palindrome(self, s: str) -> bool:
        # write your code here

        dp = {}

        for i in s:
            if i not in dp:
                dp[i] = 1
            else:
                dp[i] += 1

        odd = 0
        even = 0
        for i in list(dp.values()):
            if i % 2 == 0:
                even+=1
            else:
                odd+=1

        if odd <= 1:
            return True
        else:
            return False
