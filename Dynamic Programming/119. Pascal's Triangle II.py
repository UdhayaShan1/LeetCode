class Solution:
    def getRow(self, numRows: int) -> List[int]:
        rows = [[1],[1,1]]
        if numRows == 0:
            return [1]
        if numRows == 1:
            return [1,1]
        for i in range(2,40):
            ref = rows[i-1]
            rows.append([])
            rows[i].append(rows[i-1][0])
            for j in range(len(ref)-1):
                rows[i].append(ref[j]+ref[j+1])
            rows[i].append(rows[i-1][-1])
            if len(rows) == numRows+1:
                break

        return rows[-1]
