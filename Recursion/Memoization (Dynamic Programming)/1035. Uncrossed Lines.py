class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        import sys
        dp = {}
        def dfs(i,j):
            if i >= len(nums1) or j >= len(nums2):
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            if nums1[i] == nums2[j]:
                y1 = dfs(i+1,j+1)+1
                y2 = dfs(i+1,j)
                y3 = dfs(i,j+1)
                dp[(i,j)] = max(y1,y2,y3)

            else:
                y1 = dfs(i+1,j)
                y2 = dfs(i,j+1)
                dp[(i,j)] = max(y1,y2)
            return dp[(i,j)]

        return(dfs(0,0))
