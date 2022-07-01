class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        temp = []
        for i in boxTypes:
            temp.append([i[1],i[0]])

        temp.sort()
        temp = temp[::-1]
        temp2 = []
        for i in temp:
            temp2.append([i[1],i[0]])
        boxTypes = temp2[:]

        count = 0
        value = 0
        for i in boxTypes:
            for j in range(i[0]):
                if count == truckSize:
                    break
                count+=1
                value+=i[1]
            if count == truckSize:
                break
        return(value)
