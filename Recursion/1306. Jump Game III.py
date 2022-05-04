class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        global bruh
        bruh = 10
        def recurse(index,alr_in):
            global bruh
            if index in alr_in:
                return False
            if index < 0 or index >= len(arr):
                return False
            if arr[index] == 0:
                bool1 = 10
                bruh = 5
                return True
            alr_in[index] = 1
            recurse(index-arr[index],alr_in)
            recurse(index+arr[index],alr_in)
        recurse(start,{})
        return bruh==5
