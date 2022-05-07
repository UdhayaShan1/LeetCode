class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = list(directions)
        count = 0
        for i in range(len(directions)-1):
            if directions[i] == "R" and directions[i+1] == "L":
                count+=2
                directions[i] = "S"
                directions[i+1] = "S"
                continue
            if directions[i] == "R" and directions[i+1] == "S":
                count+=1
                directions[i] = "S"
                directions[i+1] = "S"
                continue
            if directions[i] == "S" and directions[i+1] == "L":
                count+=1
                directions[i] = "S"
                directions[i+1] = "S"
                continue

        for i in range(len(directions)-1,0,-1):
            if directions[i-1] == "R" and directions[i] == "S":
                count+=1
                directions[i] = "S"
                directions[i-1] = "S"
                continue
        return(count)
