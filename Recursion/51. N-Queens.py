class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        import copy
        res = []
        for i in range(n):
            res.append([])
            for j in range(n):
                res[i].append(".")


        res2 = res[:]

        res4 = []

        def recurse(k1,res):
            if k1 >= len(res):
                res4.append(copy.deepcopy(res))
                return

            for i in range(len(res)):
                res3 = copy.deepcopy(res)
                if res3[k1][i] == "B":
                    continue
                res3[k1][i] = "Q"
                for j in range(len(res)):
                    if j == k1:
                        continue
                    res3[j][i] = "B"

                dp2 = {}
                def dfs(i,j):
                    if i < 0 or j < 0 or i >= len(res3) or j >= len(res3):
                        return 0
                    if (i,j) in dp2:
                        return 0
                    res3[i][j] = "B"

                    dp2[(i,j)] = 1

                    y5 = dfs(i+1,j+1)
                    y8 = dfs(i-1,j-1)
                    del dp2[(i,j)]

                dfs(k1,i)

                dp2 = {}
                def dfs(i,j):
                    if i < 0 or j < 0 or i >= len(res3) or j >= len(res3):
                        return 0
                    if (i,j) in dp2:
                        return 0
                    res3[i][j] = "B"

                    dp2[(i,j)] = 1


                    y6 = dfs(i-1,j+1)
                    y7 = dfs(i+1,j-1)

                    del dp2[(i,j)]

                dfs(k1,i)


                res3[k1][i] = "Q"

                recurse(k1+1,res3)

        recurse(0,res)
        final = []
        for i in range(len(res4)):
            final.append([])
            for j in res4[i]:
                temp = j.copy()
                temp2 = []
                for k in temp:
                    if k == "B":
                        temp2.append(".")
                    else:
                        temp2.append("Q")
                final[i].append(''.join(temp2))
        return(final)
