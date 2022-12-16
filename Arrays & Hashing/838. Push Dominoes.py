class Solution:
    def pushDominoes(self, arr: str) -> str:
        left = []
        right = []
        to_add = 0
        for i in range(len(arr)):
            if arr[i] == "L":
                to_add = 0
                right.append(0)
            elif arr[i] == "R":
                to_add = 1
                right.append(0)
            else:
                if to_add == 1:
                    if i == 0:
                        right.append(0)
                    else:
                        right.append(1+right[i-1])
                else:
                    right.append(0)
        to_add = 0
        count = 0
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == "L":
                to_add = 1
                left.append(0)
                count+=1
            elif arr[i] == "R":
                to_add = 0
                left.append(0)
                count+=1
            else:
                if to_add == 1:
                    if count == 0:
                        left.append(0)
                        count+=1
                    else:
                        left.append(1+left[count-1])
                        count+=1
                else:
                    left.append(0)
                    count+=1
        left = left[::-1]

        str1 = ""
        for i in range(len(arr)):
            if arr[i] == "L" or arr[i] == "R":
                str1+=(arr[i])
            else:
                if left[i] == 0 and right[i] > 0:
                    str1+="R"
                elif left[i] > 0 and right[i] == 0:
                    str1+="L"
                else:
                    if left[i] < right[i]:
                        str1+="L"
                    elif right[i] < left[i]:
                        str1+="R"
                    else:
                        str1+="."
        return(str1)
