class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if list(s)[::-1] == list(s):
            return 1
        return 2
