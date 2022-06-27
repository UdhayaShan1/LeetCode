#Solved on codingninjas.com

def factorCombinations(n):
    res = []
    def dfs(n,arr,start):
        if n <= 1:
            res.append(arr[:])
            return True
        
        for i in range(start,n+1):
            if n % i == 0:
                arr.append(i)
                dfs(n//i,arr,i)
                arr.pop()
    dfs(n,[],2)
    return res[:-1]
 
        
    pass
