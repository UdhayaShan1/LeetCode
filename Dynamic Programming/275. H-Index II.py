class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = len(citations)-1
        b1 = False
        while b1==False:
            middle = (start+end)//2
            ref = citations[middle]
            if abs(start-end)<=1:
                break
            if ref >= (len(citations)-middle):
                end = middle
                continue
            if ref < (len(citations)-middle):
                start = middle+1
                continue
        for i in [start,end]:
            ref = citations[i]
            if ref >= (len(citations)-i):
                return (len(citations)-i)
        return 0
