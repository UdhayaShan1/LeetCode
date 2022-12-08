class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        count = 0
        b1 = False
        while b1==False:
            if left == right:
                count+=1
                break
            if left > right:
                break
            if people[left]+people[right] > limit:
                right -= 1
                count+=1
                continue
            if people[left]+people[right] <= limit:
                left+=1
                right-=1
                count+=1
                continue
        return(count)
