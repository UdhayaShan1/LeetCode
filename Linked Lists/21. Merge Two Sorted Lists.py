# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        curr_a = list1
        curr_b = list2
        while curr_a and curr_b:
            if curr_a.val < curr_b.val:
                curr.next = curr_a
                curr_a = curr_a.next
                curr = curr.next
            else:
                curr.next = curr_b
                curr_b = curr_b.next
                curr = curr.next
        if curr_a:
            curr.next = curr_a
        elif curr_b:
            curr.next = curr_b
        return dummy.next
