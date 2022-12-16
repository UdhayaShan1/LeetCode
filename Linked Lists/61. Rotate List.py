# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        k = k % length
        if k == 0:
            return head
        curr = head
        for i in range(length-k-1):
            curr = curr.next
        newHead = curr.next
        
        tmp = newHead
        for i in range(k-1):
            tmp = tmp.next
        tmp.next = head
        curr.next = None
        return newHead
