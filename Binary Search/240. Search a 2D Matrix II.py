from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        list1 = []
        for i in matrix:
            list1 += i

        list1.sort()

        def BinarySearch(a, x):
            i = bisect_left(a, x)
            if i:
                return (i-1)
            else:
                return -1

        res = BinarySearch(list1,target+1)

        if res == -1:
            return(False)
        else:
            if list1[res] != target:
                return(False)
            else:
                return(True)
