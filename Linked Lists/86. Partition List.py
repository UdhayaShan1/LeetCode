# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        curr1 = left
        curr = head
        
        right = ListNode(0)
        curr2 = right
        while curr:
            if curr.val < x:
                curr1.next = curr
                curr1 = curr
            else:
                curr2.next = curr
                curr2 = curr
            curr = curr.next
        curr1.next = right.next
        curr2.next = None
        return left.next
        
