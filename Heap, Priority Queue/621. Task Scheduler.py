class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict1 = {}
        for i in tasks:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        dict2 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
        str1 = ""
        for i in list(dict2.keys())[::-1]:
            str1 += i*dict2[i]

        def check(dict1):
            for i in dict1:
                if dict1[i] > 0:
                    return False
            return True

        print(str1)
        final = []
        for i in range(len(str1)):
            temp3 = dict1.copy()
            temp4 = {k: v for k, v in sorted(temp3.items(), key=lambda item: item[1])}
            x = list(temp4.keys())[-1]
            if dict1[list(temp4.keys())[-1]] == 0:
                continue
            final.append(list(temp4.keys())[-1])
            dict1[x] -= 1
            if check(dict1) == True:
                break
            set1 = set()
            for j in dict1:
                if j == x:
                    continue
                if dict1[j] > 0:
                    set1.add(j)
            temp = {}
            for j in set1:
                temp[j] = dict1[j]
            temp2 = {k: v for k, v in sorted(temp.items(), key=lambda item: item[1])}
            set1 = list(temp2.keys())[::-1]
            b1 = False
            count = 0
            while b1==False:
                if check(dict1) == True:
                    break
                if count == n:
                    break
                if len(set1) == 0:
                    final.append(0)
                    count+=1
                    continue
                final.append(set1[0])
                dict1[set1[0]] -= 1
                set1.pop(0)
                count += 1
            if check(dict1) == True:
                break

        return len(final)
