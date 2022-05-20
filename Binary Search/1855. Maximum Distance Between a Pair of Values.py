from bisect import bisect_left
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        temp2 = nums2[::-1]
        temp2.sort()

        def BinarySearch(a, x):
            i = bisect_left(a, x)
            if i:
                return (i-1)
            else:
                return -1

        res = BinarySearch(temp2, 30)
        max1 = 0
        for i in range(len(nums1)):
            res = len(nums2)-1-(BinarySearch(temp2,nums1[i])+1)
            if res-i>max1:
                max1=res-i

        return(max1)
    
    
    
