class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global count
        global dp
        def recurse(i,j,pos):
            global count
            global dp
            if pos == len(word):
                count = 1
                return True
            if pos > len(word):
                return False
            if i >= len(board) or i < 0:
                return False
            if j >= len(board[0]) or j < 0:
                return False

            if (i,j) in dp:
                return False

            dp[(i,j)] = 1
            if board[i][j] == word[pos]:
                recurse(i+1,j,pos+1)
                recurse(i,j+1,pos+1)
                recurse(i-1,j,pos+1)
                recurse(i,j-1,pos+1)
            del dp[(i,j)]

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                dp = {}
                if board[i][j] != word[0]:
                    continue
                recurse(i,j,0)
                if count > 0:
                    break

        return(count)
