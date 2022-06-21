class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:


        products.sort()

        res = []
        b1 = False
        start = 1
        while b1==False:
            temp = searchWord[:start]
            prod = products[:]

            c1 = False
            while c1==False:
                middle = len(prod)//2
                if len(prod) <= 6:
                    break
                if prod[middle][0:len(temp)] == temp:
                    prod = prod[:middle+3]
                    continue
                if prod[middle][0:len(temp)] != temp:
                    if prod[middle][0:len(temp)] > temp:
                        prod = prod[:middle]
                        continue
                    if prod[middle][0:len(temp)] < temp:
                        prod = prod[middle+1:]
                        continue

            final = []
            for i in prod:
                if i[0:len(temp)] == temp:
                    final.append(i)


            res.append(final[0:3])
            start+=1
            if start == len(searchWord)+1:
                break

        return(res)
