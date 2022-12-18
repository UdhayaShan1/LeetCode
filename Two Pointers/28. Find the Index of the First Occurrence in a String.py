class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            tmp = haystack[i:i+len(needle)]
            if tmp == needle:
                return i
        return -1
