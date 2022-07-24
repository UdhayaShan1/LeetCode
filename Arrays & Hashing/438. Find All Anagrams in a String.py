class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        dp_ref = {}

        for i in p:
            if i not in dp_ref:
                dp_ref[i] = 1
            else:
                dp_ref[i] += 1

        def compare(dp_ref,dp_curr):
            for i in dp_curr.keys():
                if i not in dp_ref:
                    return False
                if dp_ref[i] != dp_curr[i]:
                    return False
            for i in dp_ref.keys():
                if i not in dp_curr:
                    return False
                if dp_ref[i] != dp_curr[i]:
                    return False
            return True

        dp_start = {}
        for i in range(0,len(p)):
            if s[i] not in dp_start:
                dp_start[s[i]] = 1
            else:
                dp_start[s[i]] += 1

        res = []
        start_index = 0
        end_index = start_index+len(p)-1
        b1 = False
        while b1==False:
            if compare(dp_ref,dp_start) == True:
                res.append(start_index)

            dp_start[s[start_index]] -= 1
            if start_index > len(s)-len(p)-1:
                break
            if dp_start[s[start_index]] == 0:
                del dp_start[s[start_index]]
            if s[end_index+1] not in dp_start:
                dp_start[s[end_index+1]] = 1
            else:
                dp_start[s[end_index+1]] += 1
            start_index+=1
            if start_index > len(s)-len(p):
                break

            end_index+=1

        return(res)
    
    
    
