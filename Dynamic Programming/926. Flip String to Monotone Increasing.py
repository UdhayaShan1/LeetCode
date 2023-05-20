class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        import functools
        @functools.lru_cache(None)
        def recurse(k1,prev):
            if k1 >= len(s):
                return 0

            if prev != "1":
                if s[k1] == "0":
                    chg = recurse(k1+1,"1")+1
                    no = recurse(k1+1,s[k1])
                    return min(chg,no)
                else:
                    chg = recurse(k1+1,"0")+1
                    no = recurse(k1+1,s[k1])
                    return min(chg,no)
            else:
                if s[k1] == "0":
                    chg = recurse(k1+1,"1")+1
                    return chg
                else:
                    no = recurse(k1+1, s[k1])
                    return no

        return(recurse(0,0))
