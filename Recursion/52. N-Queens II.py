class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        board = []
        for i in range(n):
            board.append([])
            for j in range(n):
                board[i].append(".")

        res = []
        import copy
        def dfs(k1,board):
            if k1 >= n:
                res.append(copy.deepcopy(board))
                return

            for i in range(n):
                if board[k1][i] == "X":
                    continue
                board2 = copy.deepcopy(board)
                for k in range(n):
                    if k == k1:
                        continue
                    board2[k][i] = "X"
                for k in range(n):
                    if k == i:
                        continue
                    board2[k1][k] = "X"

                dp2 = {}
                def diag1(i,j):
                    if i < 0 or j < 0 or i >= n or j >= n:
                        return
                    if (i,j) in dp2:
                        return
                    board2[i][j] = "X"

                    dp2[(i,j)] = 1
                    y1 = diag1(i+1,j+1)
                    y2 = diag1(i-1,j-1)
                    del dp2[(i,j)]
                diag1(k1,i)

                dp2 = {}
                def diag2(i,j):
                    if i < 0 or j < 0 or i >= n or j >= n:
                        return
                    if (i,j) in dp2:
                        return
                    board2[i][j] = "X"

                    dp2[(i,j)] = 1
                    y1 = diag2(i-1,j+1)
                    y2 = diag2(i+1,j-1)
                    del dp2[(i,j)]
                diag2(k1,i)

                board2[k1][i] = "Q"
                dfs(k1+1,board2)
        dfs(0,board)
        return len(res)
