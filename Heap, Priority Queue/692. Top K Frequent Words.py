class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1 = {}
        for i in words:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        dict2 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
        final = []
        max1 = 10000000
        count = -1
        for i in list(dict2.keys())[::-1]:
            if dict2[i] < max1:
                final.append([])
                count+=1
                max1 = dict2[i]
                final[count].append(i)
            elif dict2[i] == max1:
                final[count].append(i)
                final[count].sort()

        final2 = []
        for i in final:
            final2+=i
            if len(final2) >= k:
                break
        return(final2[:k])
