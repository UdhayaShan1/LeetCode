# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        flag = 0
        curr = head
        dp = {}
        while curr:
            if curr in dp:
                flag+=1
                break
            dp[curr] = 1
            curr = curr.next
        if flag == 1:
            return True
        return False
