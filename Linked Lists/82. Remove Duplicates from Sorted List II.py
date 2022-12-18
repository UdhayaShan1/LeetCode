# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        curr1 = head
        while curr1:
            if curr1.next and (curr1.val == curr1.next.val):
                while curr1.next and (curr1.val == curr1.next.val):
                    curr1 = curr1.next
                curr.next = curr1.next
            else:
                curr.next = curr1
                curr = curr1
            curr1 = curr1.next
        return dummy.next
                    
