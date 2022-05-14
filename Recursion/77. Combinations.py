class Solution:
    def combine(self, n: int, k1: int) -> List[List[int]]:
        list1 = []
        for i in range(1,n+1):
            list1.append(int(i))
            
        res = []

        def Combinations(arr,k):
            if len(arr) == k1:
                res.append(arr.copy())
                return True
            if len(arr) > k1:
                return False
            for i in range(k,n+1):
                arr.append(i)
                Combinations(arr,i+1)
                arr.pop()

        Combinations([],1)
        return(res)
