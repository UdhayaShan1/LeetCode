#Solved on codingninjas.com

def tossStrangeCoins(prob, target):
    # Write your code here.
    import sys
    dp = {}
    def dfs(k1,heads_count,tail_count):
        if heads_count == target and tail_count == len(prob)-target:
            return 1
        if heads_count > target or k1 >= len(prob):
            return 0
        if (k1,heads_count,tail_count) in dp:
            return dp[(k1,heads_count,tail_count)]


        heads = dfs(k1+1,heads_count+1,tail_count)*prob[k1]
        tails = dfs(k1+1,heads_count,tail_count+1)*(1-prob[k1])
        dp[(k1,heads_count,tail_count)] = heads+tails
        return heads+tails

    return(dfs(0,0,0))
    
    pass
