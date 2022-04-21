class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        dp_row = {}
        dp_column = {}
        flag = 0
        for i in range(9):
            dp_row[i] = []
            dp_column[i] = []
            for j in board[i]:
                if j == ".":
                    continue
                if j not in dp_row[i]:
                    dp_row[i].append(j)
                else:
                    dp_row[i].append(j)
                    flag+=1
                    break
            if flag > 0:
                break
            for j in board:
                if j[i] == ".":
                    continue
                if j[i] not in dp_column[i]:
                    dp_column[i].append(j[i])
                else:
                    flag+=1
                    break
            if flag > 0:
                break

        if flag > 0:
            return(False)
        else:




            def check(start_row,start_column):
                dp = {}
                dp[board[start_row][start_column]] = 1

                if board[start_row-1][start_column-1] in dp and board[start_row-1][start_column-1] != ".":
                    return False
                else:
                    dp[board[start_row-1][start_column-1]] = 1


                if board[start_row-1][start_column] in dp and board[start_row-1][start_column] != ".":
                    return False
                else:
                    dp[board[start_row-1][start_column]] = 1

                if board[start_row-1][start_column+1] in dp and board[start_row-1][start_column+1] != ".":
                    return False
                else:
                    dp[board[start_row-1][start_column+1]] = 1



                ##

                if board[start_row][start_column-1] in dp and board[start_row][start_column-1] != ".":
                    return False
                else:
                    dp[board[start_row][start_column-1]] = 1


                if board[start_row][start_column+1] in dp and board[start_row][start_column+1] != ".":
                    return False
                else:
                    dp[board[start_row][start_column+1]] = 1

                ##

                if board[start_row+1][start_column-1] in dp and board[start_row+1][start_column-1] != ".":
                    return False
                else:
                    dp[board[start_row+1][start_column-1]] = 1

                if board[start_row+1][start_column] in dp and board[start_row+1][start_column] != ".":
                    return False
                else:
                    dp[board[start_row+1][start_column]] = 1

                if board[start_row+1][start_column+1] in dp and board[start_row+1][start_column+1] != ".":
                    return False
                else:
                    dp[board[start_row+1][start_column+1]] = 1

                return True


            b1 = False
            start_row = 1
            while b1==False:
                start_column = 1
                flag = 0
                for i in range(3):

                    if check(start_row,start_column) == False:
                        flag += 1
                        break
                    start_column += 3
                start_row+=3
                if flag > 0:
                    break
                if start_row > 7:
                    break

            if flag > 0:
                return(False)
            else:
                return(True)
        
