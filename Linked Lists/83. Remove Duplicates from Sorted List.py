# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dp = {}
        dummy = ListNode(0,next=head)
        curr = dummy
        while curr.next:
            if curr.next.val in dp:
                curr.next = curr.next.next
            else:
                dp[curr.next.val] = 1
                curr = curr.next
        return dummy.next
