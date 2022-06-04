class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        rows = [[1],[1,1]]
        for i in range(2,numRows):
            ref = rows[i-1]
            rows.append([])
            rows[i].append(rows[i-1][0])
            for j in range(len(ref)-1):
                rows[i].append(ref[j]+ref[j+1])
            rows[i].append(rows[i-1][-1])

        return(rows)
