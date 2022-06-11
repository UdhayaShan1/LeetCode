class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        to_find = sum(nums) - x

        track_sum = 0
        track_list = []
        min1 = -1
        for i in range(len(nums)):
            track_sum += nums[i]
            track_list.append(nums[i])
            if track_sum > to_find:
                b1 = False
                while b1==False:
                    track_sum -= track_list[0]
                    track_list.pop(0)
                    if track_sum <= to_find or len(track_list) <= 0:
                        break
            if track_sum == to_find:
                if len(track_list) > min1:
                    min1 = len(track_list)
        if min1 == -1:
            return -1
        else:
            return len(nums) - min1
