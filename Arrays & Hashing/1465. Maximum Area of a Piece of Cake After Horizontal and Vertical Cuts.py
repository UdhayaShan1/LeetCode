class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_hor = max(h-horizontalCuts[-1],horizontalCuts[0])
        max_ver = max(w-verticalCuts[-1],verticalCuts[0])
        
        for i in range(len(horizontalCuts)-1):
            if horizontalCuts[i+1]-horizontalCuts[i] > max_hor:
                max_hor = horizontalCuts[i+1]-horizontalCuts[i]
                
        for i in range(len(verticalCuts)-1):
            if verticalCuts[i+1]-verticalCuts[i] > max_ver:
                max_ver = verticalCuts[i+1]-verticalCuts[i]
                
        return (max_ver*max_hor)%(10**9+7)
