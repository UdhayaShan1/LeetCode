class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dp2 = {}
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
            if board[i][j] == "X" or board[i][j] == "P":
                return
            if board[i][j] in dp2:
                return
            board[i][j] = "P"

            dp2[(i,j)] = 1
            y1 = dfs(i+1,j)
            y2 = dfs(i-1,j)
            y3 = dfs(i,j+1)
            y4 = dfs(i,j-1)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1:
                    if board[i][j] == "O":
                        dfs(i,j)
                if j == 0 or j == len(board[0])-1:
                    if board[i][j] == "O":
                        dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"
