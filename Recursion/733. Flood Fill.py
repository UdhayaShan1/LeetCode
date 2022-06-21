class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(i,j,prev):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                return 0
            if image[i][j] == color:
                return 0
            if image[i][j] != prev:
                return 0

            initial = image[i][j]
            image[i][j] = color

            y1 = dfs(i+1,j,initial)
            y2 = dfs(i-1,j,initial)
            y3 = dfs(i,j+1,initial)
            y4 = dfs(i,j-1,initial)
        dfs(sr,sc,image[sr][sc])
        return(image)
